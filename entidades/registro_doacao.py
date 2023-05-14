from datetime import date
from entidades.animal import Animal
from entidades.doador import Doador


class RegistroDoacao:
    def __init__(self, codigo_registro: int, data: date, animal: Animal, doador: Doador, motivo: str):
        self.__data = data
        if isinstance(codigo_registro, int):
            self.__codigo_registro = codigo_registro
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(doador, Doador):
            self.__doador = doador
        if isinstance(motivo, str):
            self.__motivo = motivo
    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @property
    def data(self):
        return self.__data

    @property
    def animal(self):
        return self.__animal

    @property
    def doador(self):
        return self.__doador

    @property
    def motivo(self):
        return self.__motivo

    @codigo_registro.setter
    def codigo_registro(self, codigo_regstro: int):
        if isinstance(codigo_regstro, int):
            self.__codigo_regstro = codigo_regstro
    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo