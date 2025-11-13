
const readlineSync = require('readline-sync');

function calcular(x, y, z) {
    let resultado;
    if (y == "+") {
        resultado = x + z; 
     } else if (y == "-") {
         resultado = x - z;
     } else if (y =="*") {
         resultado = x * z;
     } else if (y == "/") {
         resultado = x / z
     }
    return 'O resultado de: '+x+y+z+' = '+resultado
}

var n1 = parseFloat(readlineSync.question('Informe um numero: '))
var n2 =  parseFloat(readlineSync.question('Informe outro numero: '))
var operador =  readlineSync.question('Informe a operecao (+, -, /, *): ')

console.log(calcular(n1, operador, n2))
