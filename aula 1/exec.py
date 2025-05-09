numeroSecreto = 7

entrada = input("Tente adivinhar o número secreto: ")

tentativa = int(entrada)

if tentativa == numeroSecreto:
    print("Parabéns, você acertou o número secreto!")
elif tentativa < numeroSecreto:
    print(f"Errou! O número secreto é maior que {tentativa}.")
else:
    print(f"Errou! O número secreto é menor que {tentativa}.")