from entidades.adotante import Adotante
from entidades.animal import Animal
from datetime import date


class RegistroAdocao:
    def __init__(self, codigo_registro: int, animal: Animal, adotante: Adotante, termo_responsabilidade: bool):
        self.__data = date.today()
        #criar uma maneira de gerar os codigos de registro
        self.__codigo_registro = codigo_registro
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
        if isinstance(termo_responsabilidade, bool):
            self.__termo_responsabilidade = termo_responsabilidade

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @property
    def animal(self):
        return self.__animal

    @property
    def adotante(self):
        return self.__adotante

    @property
    def termo_responsabilidade(self):
        return self.__termo_responsabilidade

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro: int):
        if isinstance(codigo_registro, int):
            self.__codigo_regstro = codigo_registro

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @adotante.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__animal = adotante

    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade: bool):
        if isinstance(termo_responsabilidade, bool):
            self.__termo_responsabilidade = termo_responsabilidade

