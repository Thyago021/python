import random

pratos = ["Churrasco", "Lasanha", "Feijoada", "Bife", "Brigadeiro", "Coxinha", "Pão de Queijo", "Escondidinho", "Strogonoff", "Hamburguer"]

prato_secreto = random.choice(pratos)

tentativas = 5

print("Bem-vindo ao jogo de adivinhar o prato secreto!")
print(f"Você tem {tentativas} tentativas para adivinhar o prato secreto.")

for tentativa in range(1, tentativas + 1):
    palpite = input(f"Tentativa {tentativa} de {tentativas}: Qual é o prato secreto? ").strip()
    
    if palpite.lower() == prato_secreto.lower():
        print("Parabéns! Você acertou o prato secreto!")
        break
    else:
        tentativas_restantes = tentativas - tentativa
        if tentativas_restantes > 0:
            print(f"Errado! Você ainda tem {tentativas_restantes} tentativas.")
        else:
            print(f"Você não acertou o prato secreto. O prato era: {prato_secreto}")