import random

def escolher_dificuldade():
    print("Escolha a dificuldade:")
    print("1 - Fácil (30 tentativas)")
    print("2 - Médio (15 tentativas)")
    print("3 - Difícil (5 tentativas)")
    
    while True:
        escolha = input("Digite o número correspondente ao nível: ")
        if escolha == '1':
            return 30, 10
        elif escolha == '2':
            return 15, 20
        elif escolha == '3':
            return 5, 50
        else:
            print("Opção inválida. Tente novamente.")

def obter_numero_jogador():
    while True:
        try:
            numero = int(input("Digite um número entre 10 e 100: "))
            if 10 <= numero <= 100:
                return numero
            else:
                print("Número fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def jogar():
    print("=== Bem-vindo ao Jogo do Número Secreto ===")
    tentativas_restantes, perda_por_erro = escolher_dificuldade()
    numero_secreto = random.randint(10, 100)
    pontuacao = 100

    while tentativas_restantes > 0:
        print(f"\nTentativas restantes: {tentativas_restantes}")
        print(f"Pontuação atual: {pontuacao}")
        chute = obter_numero_jogador()

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto}!")
            print(f"Pontuação final: {pontuacao}")
            break
        else:
            tentativas_restantes -= 1
            pontuacao -= perda_por_erro
            if chute < numero_secreto:
                print("O número secreto é maior!")
            else:
                print("O número secreto é menor!")

    if tentativas_restantes == 0 and chute != numero_secreto:
        print(f"\nVocê perdeu! O número secreto era {numero_secreto}.")
        print(f"Pontuação final: {pontuacao}")

# Iniciar o jogo
jogar()