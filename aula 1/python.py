time = input("Qual é o seu time?")

print("O seu time é:", time)
print("")
nome = "Thyago"

#formas de sída de informação
#primeira forma
print('primeira forma:', time, nome)

#segunda forma
print(f"segunda forma: {time} {nome}")

#terceira forma
print("terceira forma: {}".format(time, nome))