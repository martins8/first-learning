const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

const app = express()
const porta = 8080

let nomes = []

app.use(cors())

app.use(bodyParser.urlencoded({extend:false}))
app.use(bodyParser.json())

app.get('/nomes', (require, response) => {
    response.send(nomes)
});

app.post('/nomes', (require, response) => {
    const nome = require.body;
    console.log(nome)
    nomes.push(nome)

    response.send('O nome foi inserido com sucesso')
})

app.listen(porta, () => {
    console.log("Servidor rodando na porta 8080")
})