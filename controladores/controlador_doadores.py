from ..entidades.doador import Doador
from ..telas.tela_doador import TelaDoador


class ControladorDoadores():
    def __init__(self, controlador_sistema):
        self.__doadores = []
        self.__tela_doador = TelaDoador()
        self.__controlador_sistema = controlador_sistema

    def pegar_doador_por_cpf(self, cpf: int):
        for doador in self.__doadores:
            if (doador.cpf == cpf):
                return doador
        return None

    def incluir(self):
        pass

    def listar_doadores(self):
        pass

    def alterar_doador(self):
        pass

    def excluir_doador(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_doador, 2: self.alterar_doador,
                        3: self.listar_doadores, 4: self.excluir_doador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_doador.tela_opcoes()]()