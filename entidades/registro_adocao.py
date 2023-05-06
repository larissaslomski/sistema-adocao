from entidades.adotante import Adotante
from entidades.animal import Animal
from datetime import date


class RegistroAdocao:
    def __init__(self, codigo_registro: int, animal: Animal, adotante: Adotante, termo_responsabilidade: bool):
        self.__data = date.today()
        if isinstance(codigo_registro, int):
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
    def termo_responsabilidade(self):
        return self.__termo_responsabilidade

    @codigo_registro.setter
    def codigo_registro(self, codigo_regstro: int):
        if isinstance(codigo_regstro, int):
            self.__codigo_regstro = codigo_regstro

    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade: bool):
        if isinstance(termo_responsabilidade, bool):
            self.__termo_responsabilidade = termo_responsabilidade

