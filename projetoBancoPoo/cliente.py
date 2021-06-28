

class Pessoa: #Classe Pai
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    #Getters

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa): #classe cliente herdando da classe Pessoa
    def __init__(self, nome, idade): #Atributos da classe
        super().__init__(nome, idade)  #Atributos herdados
        self.conta = None #Atributo específico da classe cliente

    def inserirConta(self, conta): #método para inserir a conta (como se fosse um setter)
        self.conta = conta





