import os

os.system("cls || clear") # Limpar terminal

class Endereco:
    # Construtor:
    def __init__(self, logradouro: str, numero: int) -> None:
        # Atributos: 
        self.logradouro = logradouro
        self.numero = numero

    # def exibir_endereco(self) -> str:
    #     return f"Logradouro: {self.logradouro} \nNúmero: {self.numero}"
    def __str__ (self) -> str:
         return f"Logradouro: {self.logradouro} \nNúmero: {self.numero}"


class Aluno:
    # nome, idade
    # Construtor:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None :
        # Atributos: 
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__ (self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nDados do endereço: \n{self.endereco}"
    
    
# Instanciar classe: 
aluno = Aluno("Marta", 22, Endereco("Rua G", 9))
# endereco = Endereco("Avenida 5", 5)
# print(f"Nome:  {aluno.nome}")
# print(f"Idade:  {aluno.idade}")

print(aluno)
# print(aluno.exibir_dados())
# print(endereco.exibir_endereco())