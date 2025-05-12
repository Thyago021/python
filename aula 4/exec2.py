""" 
desafio: remover duplicatas: dada a lista elementos = [5,2,5,8,1,8,3] crie uma nova lista contendo apenas os elementos únicos da lista original, mantendo a ordem original de aparição e imprima a nova lista
 """

elementos = [5,2,5,8,1,8,3]
semDuplicatas = []

for i in elementos:
    if i not in semDuplicatas:
        semDuplicatas.append(i)
print("lista:", semDuplicatas)