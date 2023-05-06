from abc import ABC, abstractmethod
from entidades.historico_vacinacao import HistoricoVacinacao

class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str, historico_vacinacao: HistoricoVacinacao):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        if isinstance(historico_vacinacao, HistoricoVacinacao):
            self.__historico_vacinacao = historico_vacinacao

    @property
    def numero_chip(self):
        return self.__numero_chip

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

    @property
    def historico_vacinacao(self):
        return self.__historico_vacinacao

    @numero_chip.setter
    def numero_chip(self, numero_chip):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @raca.setter
    def raca(self, raca):
        if isinstance(raca, str):
            self.__raca = raca

    @historico_vacinacao.setter
    def historico_vacinacao(self, historico_vacinacao):
        if isinstance(historico_vacinacao, HistoricoVacinacao):
            self.__historico_vacinacao = historico_vacinacao