from entidades.animal import Animal
from entidades.historico_vacinacao import HistoricoVacinacao
import uuid


class Cachorro(Animal):
    #incluir historico de vacinacao no init e super(classe super tmb)
    def __init__(self, num_chip: int, nome: str, raca: str, tamanho: str):
        super().__init__(num_chip, nome, raca)
        if isinstance(tamanho, str):
            self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho
