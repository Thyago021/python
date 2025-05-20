 #criando o nosso primeiro modelo (Classe)
class Cachorro:
    #método Construtor
    def __init__(self,raca_cao,nome_cao,idade_cao):
        self.raca = raca_cao
        self.nome = nome_cao
        self.idade = idade_cao


    #métodos (funções Metidas)
    def latir(self):
        print("Au Au!")

##usa o modelo (Instancia)
cachorro_um = Cachorro("Golden","MadMax",10)
print(f"a raça do meu cachorro é: {cachorro_um.raca}")
cachorro_um.latir()

cachorro_dois = Cachorro("Poodle","Fifi",15)
cachorro_dois.latir()
print(f"O nome do cachorro dois é: {cachorro_dois.nome}")