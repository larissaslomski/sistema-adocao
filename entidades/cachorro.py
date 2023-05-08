from entidades.animal import Animal
from entidades.historico_vacinacao import HistoricoVacinacao


class Cachorro(Animal):
    def __init__(self, num_chip: int, nome: str, raca: str, historico_vacinacao: HistoricoVacinacao, tamanho: str):
        super().__init__(num_chip, nome, raca, historico_vacinacao)
        if isinstance(tamanho, str):
            self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho
