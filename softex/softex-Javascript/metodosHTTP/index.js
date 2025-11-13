

const express = require('express');
const app = express();

app.listen(8965, ()=>{
    console.log("Servidor iniciado")
})

app.get('/testget', (request, response)=>{
    response.send('METODO GET')
})

app.get('/testget2', (request, response)=>{
    return response.json("METODO GET 2")
})