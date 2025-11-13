var nota1;
var nota2;
var nota3;
var media;
var situacao;

function analisarSituacao() {
    
    nota1 = parseFloat(document.getElementById('nota1').value);
    nota2 = parseFloat(document.getElementById('nota2').value);
    nota3 = parseFloat(document.getElementById('nota3').value);
    media = (nota1 + nota2 + nota3) / 3;
    situacao = (media >= 7) ?  "Aprovado" : "Reprovado";
    document.getElementById('situacao').innerHTML = "Sua situação acadêmica: "+situacao;
    document.getElementById('media').innerHTML = "Sua média: "+media;
}

var nota_1;
var nota_2;
var nota_necessaria;
function analisarNotaNecessaria() {
    nota_1 = parseFloat(document.getElementById('nota_1').value);
    nota_2 = parseFloat(document.getElementById('nota_2').value);
    nota_necessaria =  21 - (nota_1+nota_2);
    document.getElementById('nota_necessaria').innerHTML = "Nota necessária: "+nota_necessaria;
}
