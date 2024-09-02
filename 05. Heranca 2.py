from abc import ABC, abstractmethod
import os

os.system ("cls || clear")

class Endereco:
    # Construtor:
    def __init__(self, logradouro: str, numero: str, complemento: str, CEP: str, cidade: str) -> None:
        # Atributos: 
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.CEP = CEP
        self.cidade = cidade

    # def exibir_endereco(self) -> str:
    #     return f"Logradouro: {self.logradouro} \nNúmero: {self.numero}"
    def __str__ (self) -> str:
         return f"Logradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.CEP} \nCidade: {self.cidade}"

class Funcionario(ABC):
    # Construtor
    def __init__(self, nome: str, idade: int, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
