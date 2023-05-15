from abc import ABC, abstractmethod
import uuid


class Animal(ABC):
    # incluir historico vacinacao no init
    @abstractmethod
    def __init__(self, num_chip: int, nome: str, raca: str):
        self.__historicos_vacinacao = []
        if isinstance(num_chip, int):
            self.__num_chip = num_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca

    @property
    def historicos_vacinacao(self):
        return self.__historicos_vacinacao

    @property
    def num_chip(self):
        return self.__num_chip

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @raca.setter
    def raca(self, raca):
        if isinstance(raca, str):
            self.__raca = raca

    @historicos_vacinacao.setter
    def historico_vacinacao(self, historico_vacinacao):
        self.__historicos_vacinacao.append(historico_vacinacao)

    def listar_vacinas_historico(self):
        lista_historico = []
        for historico_vacinacao in self.__historicos_vacinacao:
            lista_historico.append(historico_vacinacao.vacina.nome_vacina)
        return lista_historico
