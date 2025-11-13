var numero1;
var numero2;
var operador;
var resultado;

function enviar() {
    

    numero1 = document.getElementById('numero1').value;
    numero2 = document.getElementById('numero2').value;
    operador = document.getElementById('operador').value;

    if (operador == "+") {
       resultado = numero1 + numero2; 
    } else if (operador == "-") {
        resultado = numero1 - numero2;
    } else if (operador =="*") {
        resultado = numero1 * numero2;
    } else if (operador == "/") {
        resultado = numero1 / numero2
    }

    document.getElementById('resultado').innerHTML = resultado;
    console.log(resultado)
}

