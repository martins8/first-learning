import React from "react"
import { Contador } from "../components/Contador"
import './styles.css'

function App() {
  return (
    <div className="App">
      <div className="container">
       <strong>UTILIZE O BOTÃO ABAIXO PARA ADICIONAR 1 NA CONTAGEM</strong>
      </div>
      <Contador/>
    </div>
  )
}

export default App
