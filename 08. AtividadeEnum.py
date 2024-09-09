import os
os.system("cls || clear")

from enum import Enum

class Setores(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Generos(Enum):
    FEMININO = "Feminino"
    MASCULINO = "Masculino"

class Funcionario:
    def __init__(self, nome: str, idade: str, salario: str, generos: Generos, setor: Setores) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.generos = generos
        self.setor = setor

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalário: {self.salario}"
                f"\nGênero: {self.generos.value}"
                f"\nSetor: {self.setor.value}")
    
funcionario1 = Funcionario("Marta", "25", "5.000", Generos.FEMININO, Setores.RECURSOS_HUMANOS)

print(funcionario1)
