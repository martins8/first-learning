import {useState} from 'react';
import './styles.css'

export function Contador(){
    const [numero, setNumero] = useState(0)
    
    function adicionar (){
        setNumero(parseFloat(numero+1))
        console.log(numero)
    }


    return(
        <div className="contador">
            <strong>{numero}</strong>
            <button onClick={adicionar}>ADICIONAR</button>
        </div>
    )
}