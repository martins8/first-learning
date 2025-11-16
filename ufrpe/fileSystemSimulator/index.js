const readline = require("readline");
const fs = require("fs");
const path = require("path");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// --- Configuração do simulador (será inicializada interativamente) ---
let BLOCK_SIZE = 4096; // bytes
let TOTAL_MEMORY = 64 * 1024; // bytes (64 KB)
let TOTAL_BLOCKS = Math.floor(TOTAL_MEMORY / BLOCK_SIZE);

// Array de blocos: cada bloco tem {id, used, owner, next, bytesUsed}
let blocks = [];

// Estrutura de diretório simples de dois níveis: root tem diretórios e arquivos; diretórios contêm apenas arquivos
const fileSystem = {
  root: {
    dirs: {}, // nome -> { name, files: { name->fileEntry } }
    files: {},
  },
  filesMap: {}, // caminhoDoArquivo -> fileEntry para busca rápida
};

function initBlocks() {
  TOTAL_BLOCKS = Math.max(1, Math.floor(TOTAL_MEMORY / BLOCK_SIZE));
  blocks = new Array(TOTAL_BLOCKS).fill(null).map((_, i) => ({
    id: i,
    used: false,
    owner: null, // caminho do arquivo
    next: -1, // índice do próximo bloco
    bytesUsed: 0,
  }));
}

function human(bytes) {
  if (bytes >= 1024) return (bytes / 1024).toFixed(2) + " KB";
  return bytes + " B";
}

// Inicializa com valores padrão
initBlocks();
// --- Alocação: alocação encadeada (linked allocation) ---
function allocateBlocksForFile(filePath, size) {
  const blocksNeeded = Math.ceil(size / BLOCK_SIZE);
  const freeBlocks = blocks.reduce((acc, b) => {
    if (!b.used) acc.push(b.id);
    return acc;
  }, []);

  if (freeBlocks.length < blocksNeeded) return null; // blocos livres insuficientes

  // pega os primeiros N blocos livres (alocação encadeada não requer contiguidade)
  const chain = freeBlocks.slice(0, blocksNeeded);
  for (let i = 0; i < chain.length; i++) {
    const idx = chain[i];
    blocks[idx].used = true;
    blocks[idx].owner = filePath;
    blocks[idx].next = i + 1 < chain.length ? chain[i + 1] : -1;
    // bytesUsed: blocos completos recebem BLOCK_SIZE, último bloco recebe o restante
    if (i === chain.length - 1) {
      const rem = size - (blocksNeeded - 1) * BLOCK_SIZE;
      blocks[idx].bytesUsed = rem;
    } else {
      blocks[idx].bytesUsed = BLOCK_SIZE;
    }
  }
  return chain;
}

function freeBlocksOfFile(filePath) {
  let freed = 0;
  blocks.forEach((b) => {
    if (b.used && b.owner === filePath) {
      b.used = false;
      b.owner = null;
      b.next = -1;
      b.bytesUsed = 0;
      freed++;
    }
  });
  return freed;
}

// --- Helpers de Arquivo / Diretório ---
function hasNameConflict(dirObj, name) {
  return !!dirObj.files[name] || !!dirObj.dirs[name];
}

function createDirectory(name) {
  if (!name) return { ok: false, msg: "Nome inválido" };
  if (fileSystem.root.dirs[name] || fileSystem.root.files[name])
    return { ok: false, msg: "Nome já existe no root" };
  fileSystem.root.dirs[name] = { name, files: {}, dirs: {} };
  return { ok: true };
}

function removeDirectory(name) {
  const dir = fileSystem.root.dirs[name];
  if (!dir) return { ok: false, msg: "Diretório não existe" };
  if (Object.keys(dir.files).length > 0)
    return { ok: false, msg: "Diretório não está vazio" };
  delete fileSystem.root.dirs[name];
  return { ok: true };
}

function createFile(pathParts, size) {
  // pathParts: [talvezDir, nome] ou [nome]
  if (size <= 0) return { ok: false, msg: "Tamanho deve ser > 0" };
  let dir = fileSystem.root;
  let fileName;
  if (pathParts.length === 2) {
    const d = pathParts[0];
    fileName = pathParts[1];
    if (!fileSystem.root.dirs[d])
      return { ok: false, msg: "Diretório não existe" };
    dir = fileSystem.root.dirs[d];
  } else {
    fileName = pathParts[0];
  }
  if (hasNameConflict(dir, fileName))
    return { ok: false, msg: "Nome já existe neste diretório" };

  const filePath =
    pathParts.length === 2 ? `${pathParts[0]}/${fileName}` : fileName;
  const chain = allocateBlocksForFile(filePath, size);
  if (!chain)
    return { ok: false, msg: "Espaço insuficiente (blocos disponíveis)" };

  const fileEntry = {
    name: fileName,
    size,
    blocks: chain,
  };
  dir.files[fileName] = fileEntry;
  fileSystem.filesMap[filePath] = fileEntry;
  return { ok: true, fileEntry };
}

function deleteFile(pathParts) {
  let dir = fileSystem.root;
  let fileName;
  if (pathParts.length === 2) {
    const d = pathParts[0];
    fileName = pathParts[1];
    if (!fileSystem.root.dirs[d])
      return { ok: false, msg: "Diretório não existe" };
    dir = fileSystem.root.dirs[d];
  } else {
    fileName = pathParts[0];
  }
  const fileEntry = dir.files[fileName];
  if (!fileEntry) return { ok: false, msg: "Arquivo não existe" };
  const filePath =
    pathParts.length === 2 ? `${pathParts[0]}/${fileName}` : fileName;
  freeBlocksOfFile(filePath);
  delete dir.files[fileName];
  delete fileSystem.filesMap[filePath];
  return { ok: true };
}

function listDirectory(dirName) {
  let dir = fileSystem.root;
  if (dirName) {
    if (!fileSystem.root.dirs[dirName])
      return { ok: false, msg: "Diretório não existe" };
    dir = fileSystem.root.dirs[dirName];
  }
  const files = Object.values(dir.files).map((f) => ({
    name: f.name,
    size: f.size,
  }));
  const dirs = dir === fileSystem.root ? Object.keys(fileSystem.root.dirs) : [];
  return { ok: true, files, dirs };
}

function getFileStat(pathParts) {
  let dir = fileSystem.root;
  let fileName;
  if (pathParts.length === 2) {
    const d = pathParts[0];
    fileName = pathParts[1];
    if (!fileSystem.root.dirs[d])
      return { ok: false, msg: "Diretório não existe" };
    dir = fileSystem.root.dirs[d];
  } else {
    fileName = pathParts[0];
  }
  const fileEntry = dir.files[fileName];
  if (!fileEntry) return { ok: false, msg: "Arquivo não existe" };
  return { ok: true, fileEntry };
}

function computeInternalFragmentation() {
  // Soma dos bytes desperdiçados no último bloco de cada arquivo
  let wasted = 0;
  for (const fp in fileSystem.filesMap) {
    const f = fileSystem.filesMap[fp];
    const rem = f.size % BLOCK_SIZE;
    if (rem !== 0) wasted += BLOCK_SIZE - rem;
  }
  return wasted;
}

function computeExternalFragmentation() {
  // Para alocação encadeada a fragmentação externa não é um problema; retorna 0 e uma explicação
  return 0;
}

function showMap() {
  console.log(
    `\nAllocation Map — Blocks: ${TOTAL_BLOCKS}, Block size: ${BLOCK_SIZE} bytes`
  );
  console.log("Idx | Used | Owner | Next | BytesUsed");
  blocks.forEach((b) => {
    console.log(
      `${b.id.toString().padStart(3)} | ${b.used ? "  X  " : "     "} | ${
        b.owner || "-"
      }` + ` | ${b.next === -1 ? "-" : b.next} | ${b.bytesUsed}`
    );
  });
  const internal = computeInternalFragmentation();
  const external = computeExternalFragmentation();
  console.log(
    `\nInternal fragmentation: ${internal} bytes (${human(internal)})`
  );
  if (external > 0) console.log(`External fragmentation: ${external} bytes`);
  else
    console.log(
      "External fragmentation: not applicable for linked allocation (0 bytes)"
    );
}

// --- Interface de Linha de Comando (CLI) ---
function printHelp() {
  console.log(`
Commands:
  help                        Show this help
  config [totalBytes] [blockBytes]  Reinitialize memory and block sizes (bytes)
  mkdir <dirname>             Create directory in root
  rmdir <dirname>             Remove empty directory in root
  create <path> <size>        Create file (path: name or dir/name) size in bytes
  del <path>                  Delete file (path: name or dir/name)
  ls [dirname]                List root or a directory
  stat <path>                 Show file blocks and details
  map                         Show allocation map and fragmentation
  exit                        Quit
`);
}

function repl() {
  rl.question("fs> ", (answer) => {
    const parts = answer.trim().split(/\s+/);
    const cmd = parts[0];
    switch (cmd) {
      case "":
        return repl();
      case "help":
        printHelp();
        break;
      case "config":
        if (parts.length >= 3) {
          const tot = parseInt(parts[1], 10);
          const blk = parseInt(parts[2], 10);
          if (isNaN(tot) || isNaN(blk) || tot <= 0 || blk <= 0)
            console.log("Valores inválidos");
          else {
            TOTAL_MEMORY = tot;
            BLOCK_SIZE = blk;
            initBlocks();
            // limpa o sistema de arquivos
            fileSystem.root = { dirs: {}, files: {} };
            fileSystem.filesMap = {};
            console.log(
              "Configurado: total",
              TOTAL_MEMORY,
              "block",
              BLOCK_SIZE,
              "blocks",
              TOTAL_BLOCKS
            );
          }
        } else console.log("Uso: config <totalBytes> <blockBytes>");
        break;
      case "mkdir":
        if (parts.length < 2) console.log("Usage: mkdir <dirname>");
        else {
          const r = createDirectory(parts[1]);
          if (!r.ok) console.log("Erro:", r.msg);
          else console.log("Diretório criado");
        }
        break;
      case "rmdir":
        if (parts.length < 2) console.log("Usage: rmdir <dirname>");
        else {
          const r = removeDirectory(parts[1]);
          if (!r.ok) console.log("Erro:", r.msg);
          else console.log("Diretório removido");
        }
        break;
      case "create":
        if (parts.length < 3) console.log("Usage: create <path> <sizeBytes>");
        else {
          const pathArg = parts[1];
          const sz = parseInt(parts[2], 10);
          if (isNaN(sz) || sz <= 0) console.log("Tamanho inválido");
          else {
            const pathParts = pathArg.split("/").filter(Boolean);
            const r = createFile(pathParts, sz);
            if (!r.ok) console.log("Erro:", r.msg);
            else
              console.log(
                "Arquivo criado:",
                r.fileEntry.name,
                "tamanho:",
                r.fileEntry.size
              );
          }
        }
        break;
      case "del":
        if (parts.length < 2) console.log("Usage: del <path>");
        else {
          const pathParts = parts[1].split("/").filter(Boolean);
          const r = deleteFile(pathParts);
          if (!r.ok) console.log("Erro:", r.msg);
          else console.log("Arquivo removido");
        }
        break;
      case "ls":
        {
          const dir = parts.length >= 2 ? parts[1] : null;
          const r = listDirectory(dir);
          if (!r.ok) console.log("Erro:", r.msg);
          else {
            if (r.dirs && r.dirs.length)
              console.log("Dirs:", r.dirs.join(", "));
            if (r.files && r.files.length) {
              console.log("Files:");
              r.files.forEach((f) =>
                console.log(`  ${f.name} — ${f.size} bytes (${human(f.size)})`)
              );
            } else console.log("(no files)");
          }
        }
        break;
      case "stat":
        if (parts.length < 2) console.log("Usage: stat <path>");
        else {
          const pathParts = parts[1].split("/").filter(Boolean);
          const r = getFileStat(pathParts);
          if (!r.ok) console.log("Erro:", r.msg);
          else {
            const f = r.fileEntry;
            console.log(
              `File ${f.name} — size ${f.size} bytes (${human(f.size)})`
            );
            console.log("Blocks chain:");
            f.blocks.forEach((bidx, i) => {
              const b = blocks[bidx];
              console.log(
                `  [${i}] block ${bidx} next=${b.next} bytesUsed=${b.bytesUsed}`
              );
            });
          }
        }
        break;
      case "map":
        showMap();
        break;
      case "exit":
        rl.close();
        return;
      default:
        console.log("Comando desconhecido. Digite 'help' para ajuda.");
    }
    return repl();
  });
}

// Boas-vindas
console.log(
  "Mini File System Simulator (Linked allocation) — two-level directories"
);
console.log(
  `Default total memory: ${TOTAL_MEMORY} bytes, block size: ${BLOCK_SIZE} bytes, blocks: ${TOTAL_BLOCKS}`
);
console.log("Type 'help' for commands.\n");
repl();
