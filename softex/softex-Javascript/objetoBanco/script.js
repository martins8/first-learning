var Banco = {
    conta: '2345-6',
    saldo: 0,
    tipo: 'corrente',
    agencia: 'x',

    buscarSaldo: function buscar_Saldo(){
        return this.saldo;
    },

    depositar: function depositar_valor(valor){
        this.saldo += valor;
    },

    sacarDinheiro: function sacar_Dinheiro(valor){
        this.saldo -= valor;
    },

    mostrarNumeroConta: function mostrar_Numero_Conta(){
        return this.conta;
    }
}

console.log(Banco.buscarSaldo());

Banco.depositar(50);
console.log(Banco.buscarSaldo());

Banco.sacarDinheiro(20);
console.log(Banco.buscarSaldo());

console.log(Banco.mostrarNumeroConta())