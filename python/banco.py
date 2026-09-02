class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        print(f"Saldo na conta {self.titular} é de: R${self.saldo}")

    def depositar(self,valor):
        print(f"Depositando R${valor} à conta {self.titular}")
        self.saldo += valor
        print(f"Saldo na conta {self.titular} ficou: R${self.saldo}")

    def sacar(self,valor):
        print(f"Sacando R${valor} à conta {self.titular}")
        if(valor<= self.saldo):
            self.saldo -= valor
            print(f"Saldo na conta {self.titular} ficou: R${self.saldo}")

        else:
            print(f"Não existe saldo o suficiente na conta {self.titular}")
print("\n-------------------------------------------------------------\n")
conta = ContaBancaria("Lucas", 580)
print("\n-------------------------------------------------------------\n")
conta.depositar(700)
print("\n-------------------------------------------------------------\n")
conta.sacar(300)
print("\n-------------------------------------------------------------\n")
conta.sacar(1850)
print("\n-------------------------------------------------------------\n")