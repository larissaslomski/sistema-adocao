from abc import ABC, abstractmethod
from entidades.historico_vacinacao import HistoricoVacinacao
import uuid


class Animal(ABC):
    #incluir historico vacinacao no init
    @abstractmethod
    def __init__(self, num_chip: int, nome: str, raca: str):
        if isinstance(num_chip, int):
            self.__num_chip = num_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        # if isinstance(historico_vacinacao, HistoricoVacinacao):
        #     self.__historico_vacinacao = historico_vacinacao

    @property
    def num_chip(self):
        return self.__num_chip

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

    # @property
    # def historico_vacinacao(self):
    #     return self.__historico_vacinacao

    # @num_chip.setter
    # def num_chip(self, num_chip):
    #     if isinstance(num_chip, int):
    #         self.__num_chip = num_chip

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @raca.setter
    def raca(self, raca):
        if isinstance(raca, str):
            self.__raca = raca

    # @historico_vacinacao.setter
    # def historico_vacinacao(self, historico_vacinacao):
    #     if isinstance(historico_vacinacao, HistoricoVacinacao):
    #         self.__historico_vacinacao = historico_vacinacao
