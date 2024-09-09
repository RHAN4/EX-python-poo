import os

os.system("cls || clear")
 
from enum import Enum

class Generos(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa: 
    """Construtor"""
    def __init__(self, nome: str, idade: str, generos: Generos) -> None:
        self.nome = nome
        self.idade = idade
        self.generos = generos

    def __str__(self) -> str:
        """Equivalente ao toString() do Java."""
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nGênero: {self.generos.value}")
    
#Instaciando classe Pessoa:

pessoa1 = Pessoa("Marta", "22", Generos.FEMININO)

print(pessoa1)

