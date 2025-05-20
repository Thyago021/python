class ContaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular
        #atributo privado
        self._saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado com sucesso!")
        else:
            print("O valor deve ser positivo!")

    def sacar(self,valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de {valor} realizada com sucesso!")
        else:
            print("Saldo insuficiente, ou falor inválido!")

    def consultar_saldo(self):
        print(f"Saldo atual: {self._saldo}")