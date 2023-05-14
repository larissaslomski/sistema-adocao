# from entidades.animal import Animal
from entidades.vacina import Vacina
from datetime import date
from entidades.animal import Animal


class HistoricoVacinacao:
    def __init__(self, data: date, animal: Animal, vacina: Vacina):
        self.__data = data
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina
