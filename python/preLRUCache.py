class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.melhor_amigo = None

    def definir_amigo(self, outra_pessoa):
        self.melhor_amigo.next = outra_pessoa
        pass

    def apresentar_amigo(self):
        if(self.melhor_amigo != None):
            print(f"O melhor amigo de {self.nome} é {self.nome}")
        pass