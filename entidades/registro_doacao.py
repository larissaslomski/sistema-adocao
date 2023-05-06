from datetime import date
from entidades.animal import Animal
from entidades.doador import Doador


class RegistroDoacao:
    def __init__(self, codigo_registro: int, animal: Animal, doador: Doador, motivo: str):
        self.__data = date.today()
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
    def motivo(self):
        return self.__motivo

    @codigo_registro.setter
    def codigo_regstro(self, codigo_regstro: int):
        if isinstance(codigo_regstro, int):
            self.__codigo_regstro = codigo_regstro
    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo