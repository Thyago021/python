class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = (titular,)
        self.saldo = [saldo_inicial]
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
        else:
            self.saldo[0] += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        elif valor > self.saldo[0]:
            print("Erro: Saldo insuficiente para o saque.")
        else:
            self.saldo[0] -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo[0]:.2f}")

    def consultar_historico(self):
        if not self.historico:
            print("Nenhuma transação realizada até o momento.")
        else:
            print("Histórico de transações:")
            for transacao in self.historico:
                print(f"- {transacao}")

def main():
    print("Bem-vindo ao sistema bancário da JWC!")
    nome = input("Digite o nome do titular da conta: ")
    while True:
        try:
            deposito_inicial = float(input("Digite o valor do depósito inicial: R$"))
            if deposito_inicial <= 0:
                print("Erro: O valor do depósito inicial deve ser positivo.")
            else:
                break
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")
    
    conta = ContaBancaria(nome, deposito_inicial)
    print(f"Conta criada com sucesso para {nome} com saldo inicial de R${deposito_inicial:.2f}.")

    while True:
        print("\nMenu de operações:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar Saldo")
        print("4. Consultar Histórico de Transações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor a ser depositado: R$"))
                conta.depositar(valor)
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor a ser sacado: R$"))
                conta.sacar(valor)
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
        elif opcao == '3':
            conta.consultar_saldo()
        elif opcao == '4':
            conta.consultar_historico()
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Erro: Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    main()