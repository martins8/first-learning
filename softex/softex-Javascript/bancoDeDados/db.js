const Sequelize = require('sequelize');
const sequelize = new Sequelize('softex', 'root', 'Aurora74583743521', 
{dialect: 'mysql', host: 'localhost'});

module.exports = sequelize;