from abc import ABC, abstractmethod
import os

os.system ("cls || clear")

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2 # Acréscimo de 20%
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1 # Acréscimo de 10%
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal
 
# Instaciar classes:
# funcionario1 = Funcionario("José", 33, 1000.0)
# print(f"Nome: {funcionario1.nome}")
# print(f"Idade: {funcionario1.idade}")
# print(f"Salário: {funcionario1.salario}")

gerente1 = Gerente("Marta", 22, 2000.0)
print(f"Nome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Salário: {gerente1.calcular_salario()}")

print("\n")

motoboy1 = Motoboy("José", 33, 1000.0, "4654621")
print(f"Nome: {motoboy1.nome}")
print(f"Idade: {motoboy1.idade}")
print(f"Salário: {motoboy1.calcular_salario()}")
print(f"Número da CNH: {motoboy1.cnh}")