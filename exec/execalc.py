def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        else:
            resultado = "Operação inválida!"

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: por favor, digite números válidos.")