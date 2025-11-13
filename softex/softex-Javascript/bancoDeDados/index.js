const database = require('./db');
const Teste = require('./testedb');

const testapp = async() => {
    
    try{
        await database.authenticate();
        console.log('Banco de dados conectado com sucesso!')
    } catch (error){
        console.log(error);
    }
}
testapp()