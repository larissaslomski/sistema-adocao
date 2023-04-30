class Pessoa:
    def __init__(self, cpf: str, nome: str, nascimento: str, endereco: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(nascimento, str) and isinstance(endereco, str):
            self.__cpf = cpf
            self.__nome = nome
            self.__nascimento = nascimento
            self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def endereco(self):
        return self.__endereco

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def cpf(self, nome):
        self.__nome = nome

    @nascimento.setter
    def cpf(self, nascimento):
        self.__nascimento = nascimento

    @endereco.setter
    def cpf(self, endereco):
        self.__endereco = endereco