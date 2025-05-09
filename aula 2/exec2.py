numero = int(input("Digite um número entre 10 e 100: "))

if numero < 10 or numero > 100:
    print("O valor deve estar entre 10 e 100.")
else:
    print(f"Contando de 0 até {numero}: ")
    for i in range(numero + 1):
        print(i)