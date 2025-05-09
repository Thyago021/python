"""
     estrutura de decisão
     classificação
        >simples
        >composta
        >encadeada
        >aninhada
"""

print("descisão simples - é dada por uma única decisão")
idade = 18

if idade >= 18:
    print("Maior de idade.")

print(15*"-")

print("composta - uma única decisão e uma resposta padrão")

if idade >= 18:
    print("maior de idade.")
else:
    print("infelizmente não posso te ajudar.")

print(15*"-")

print("encadeada - é dada por mais de uma decisão e uma resposta padrão")

if idade >= 18:
    print("maior de idade.")
elif idade <= 18:
    print("menor de idade.")
else:
    print("infelizmente não posso te ajudar.")

print(15*"-")

print("aninhada - possui uma estrutura de decisão dentro da outra")

classificacao = 18
ingresso = True

if classificacao >= 16:
    if ingresso == True:
        print("você pode assistir o filme.")
    else:
        print("você não pode assistir ao filme")
else:
    print("você não pode entrar")

print(15*"-")