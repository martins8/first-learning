const Sequelize = require('sequelize');
const database = require('./db')

const Teste = database.define('produto', {
    id: {
        type: Sequelize.INTEGER,
        autoincrement: true,
        allowNull: false,
        primaryKey: true
    },
    texto: {
        type: Sequelize.STRING,
        allowNull: false
    }
})

module.exports = Teste;