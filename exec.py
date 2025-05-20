class Tabuada:
    def __init__(self, numero):
        self.numero = numero
        self.__resultado = []

    def soma(self):
        self.__resultado = []
        print(f"\nTabuada de Soma do {self.numero}")
        for i in range(1, 11):
            resultado = self.numero + i
            self.__resultado.append(resultado)
            print(f"{self.numero} + {i} = {resultado}")

    def subtracao(self):
        self.__resultado = []
        print(f"\nTabuada de Subtração do {self.numero}")
        for i in range(1, 11):
            resultado = self.numero - i
            self.__resultado.append(resultado)
            print(f"{self.numero} - {i} = {resultado}")

    def multiplicacao(self):
        self.__resultado = []
        print(f"\nTabuada de Multiplicação do {self.numero}")
        for i in range(1, 11):
            resultado = self.numero * i
            self.__resultado.append(resultado)
            print(f"{self.numero} x {i} = {resultado}")

    def divisao(self):
        self.__resultado = []
        print(f"\nTabuada de Divisão do {self.numero}")
        for i in range(1, 11):
            resultado = self.numero / i
            self.__resultado.append(resultado)
            print(f"{self.numero} ÷ {i} = {resultado:.2f}")


if __name__ == "__main__":
    numero_usuario = int(input("Digite um número para ver a tabuada: "))
    tabuada = Tabuada(numero_usuario)
    
    tabuada.soma()
    tabuada.subtracao()
    tabuada.multiplicacao()
    tabuada.divisao()