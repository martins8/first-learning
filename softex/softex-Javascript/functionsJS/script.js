
function menuCalculadora(){
    let numero = 10;
    console.log('CALCULADORA!\no número 10 será passado por parâmetro como um multiplicando de uma operação matemática')
    passarParametro(numero)
}

function passarParametro(x){
    let y = 5;
    let operador = "*"; 
    var resultado = calcular(x, y, operador);
    console.log(resultado);
}

const calcular = (x, y, z) => "Resultado de: "+x+z+y+" = "+eval(`${x} ${z} ${y}`)



menuCalculadora();

