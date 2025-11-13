import React from "react";
import { useState } from "react";
import './Calculadora.css'

export function Calculadora(){
    const [numero1, setNumero1] = useState(0);
    const [numero2, setNumero2] = useState(0);
    const [resultado, setResultado] = useState(0)
    const [operador, setOperador] = useState('')
    
    function numeroInput1(input){
        setNumero1(input.target.value)
        console.log(input)
    }
    function numeroInput2(input){
        setNumero2(input.target.value)
        console.log(input)
    }
    
    function operando(op){
        setOperador(op.target.value)
    }

    function calcular(){
        if (operador === '+'){
            setResultado(parseFloat(numero1) + parseFloat(numero2))
        } else if (operador === '-'){
            setResultado(parseFloat(numero1) - parseFloat(numero2))
        } else if (operador === '*'){
            setResultado(parseFloat(numero1) * parseFloat(numero2))
        } else if (operador === '/'){
            setResultado(parseFloat(numero1) / parseFloat(numero2))
        }
    }

     

    return (
        <div className="calculadora">
            <div className="container">
                <input type="text" placeholder="Digite um número" onChange={e => numeroInput1(e)}/>
                <input type="text" placeholder="Digite outro número" onChange={e => numeroInput2(e)}/>
                <div className="operadores">
                    <button onClick={operando} value={'+'}>+</button>
                    <button onClick={operando} value={'-'}>-</button>
                    <button onClick={operando} value={'*'}>*</button>
                    <button onClick={operando} value={'/'}>/</button>
                </div>
                <button onClick={calcular}>CALCULAR</button>
                <p>{resultado}</p>
            </div>
        </div>
    );
}