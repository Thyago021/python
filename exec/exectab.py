def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("-" * 20)

if __name__ == "__main__":
    try:
        numero_usuario = int(input("Digite um número inteiro para ver a tabuada: "))
        mostrar_tabuada(numero_usuario)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")