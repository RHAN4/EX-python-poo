import os

os.system("cls || clear")

#Criando sua própria excessão:
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativo(Exception):
    pass
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
        # try - except
        try:
            self.__verificarSacar(valor)
        except SaldoInsuficienteError as error:
            return f"{error}"

        self._saldo -= valor
        return self._saldo

    def __verificarSacar(self, valor): # Método privado.
            if valor > self.saldo:
                raise SaldoInsuficienteError ("Saldo insuficiente.") # Lançando um erro.
            
    def depositar(self, valor):
        try:
            self.__verificarDepositar(valor)
        except ValorNegativo as error:
            return f"Erro: {error}"
        self._saldo -= valor
        return self._saldo
    
    def __verificarDepositar(self, valor):
        if valor < 0:
            raise ValorNegativo ("Não é possível depositar este valor.")
        
class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciar classes:
contaCorrente = ContaCorrente(222, 333)
contaPoupanca = ContaPoupanca(444, 555)

#Private:
#print(contaCorrente._saldo)

print(contaCorrente.saldo)
print(contaCorrente.sacar(200))
print(contaCorrente.depositar(-200))