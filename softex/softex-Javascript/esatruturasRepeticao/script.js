var Pessoa = {
    nome: 'Arthur Martins de Lima',
    idade: '21',
    cpf: '111.111.111-11',
}

var cidades = ['Recife', 'Caruaru', 'Arcoverde'];

function mostrarPropriedades(){
    for (var propriedade in Pessoa) {
        console.log(`${propriedade}: ${Pessoa[propriedade]}`)
    }
}

function mostrarElementosArray(){
    for (var element of cidades){
        console.log(element)
    }
}

mostrarPropriedades();
mostrarElementosArray();