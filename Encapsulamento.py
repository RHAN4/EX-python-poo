import os

os.system("cls || clear")

class Conta:
    def __init__(self, numeroConta: int, agencia: int) -> None:
        #Atributos
        self.numeroConta = numeroConta
        self.agencia = agencia
        self._saldo = 0 #Atributo protegido.

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise f"Saldo insuficiente." # Lançando um erro.
        self._saldo -= valor
        return self._saldo

    def depositar(self, valor):
        self._saldo -= valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar classes:
contaCorrente = ContaCorrente(222, 333)
contaPoupanca = ContaPoupanca(444, 555)

#Private:
#print(contaCorrente._saldo)

contaCorrente._saldo -= 200

print(contaCorrente.sacar(200))