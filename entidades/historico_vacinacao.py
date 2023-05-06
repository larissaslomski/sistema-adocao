from entidades.animal import Animal
from entidades.vacina import Vacina
from datetime import date


class HistoricoVacinacao:
    def __init__(self, animal: Animal, vacina: Vacina):
        self.__data = date.today()
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(vacina, Vacina):
            self.__vacina = vacina