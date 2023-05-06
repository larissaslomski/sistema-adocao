from ..telas.tela_sistema import TelaSistema
from .controlador_adotantes import ControladorAdotantes
from .controlador_doadores import ControladorDoadores
from .controlador_cachorros import ControladorCachorros
from .controlador_gatos import ControladorGatos
from .controlador_historicos_vacinacao import ControladorHistoricos
from .controlador_registros_adocao import ControladorRegistrosAdocao
from .controlador_registros_doacao import ControladorRegistrosDoacao
from .controlador_tipos_habitacao import ControladorTiposHabitacao
from .controlador_vacinas import ControladorVacinas


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_adotantes = ControladorAdotantes(self)
        self.__controlador_doadores = ControladorDoadores(self)
        self.__controlador_cachorros = ControladorCachorros(self)
        self.__controlador_gatos = ControladorGatos(self)
        self.__controlador_historicos_vacinacao = ControladorHistoricos(self)
        self.__controlador_registros_adocao = ControladorRegistrosAdocao(self)
        self.__controlador_registros_doacao = ControladorRegistrosDoacao(self)

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    @property
    def controlador_doadores(self):
        return self.__controlador_doadores

    @property
    def controlador_cachorros(self):
        return self.__controlador_cachorros

    @property
    def controlador_gatos(self):
        return self.__controlador_gatos

    def inicia_sistema(self):
        self.abre_tela()

    # 1 - Abre a tela de cadastro de Adotantes
    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()

    # 2 - Abre a tela de cadastro de Doadores
    def cadastra_doadores(self):
        self.__controlador_doadores.abre_tela()

    # 3 - Abre a tela de cadastro de Cachorros
    def cadastra_cachorros(self):
        self.__controlador_cachorros.abre_tela()

    # 4 - Abre a tela de cadastro de Gatos
    def cadastra_gatos(self):
        self.__controlador_gatos.abre_tela()

    # 5 - Abre a tela de cadastro de Registros de Adocao
    def cadastra_registros_adocao(self):
        self.__controlador_registros_adocao.abre_tela()

    # 6 - Abre a tela de cadastro de Registros de Doacao
    def cadastra_registros_doacao(self):
        self.__controlador_registros_doacao.abre_tela()

    # 7 - Abre a tela de cadastro de Historicos de Vacinacao
    def cadastra_historicos_vacinacao(self):
        self.__controlador_historicos_vacinacao.abre_tela()

    # 0 - Encerra o Sistema
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_adotantes, 2: self.cadastra_doadores,
                        3: self.cadastra_cachorros, 4: self.cadastra_gatos,
                        5: self.cadastra_registros_adocao, 6: self.cadastra_registros_doacao,
                        7: self.cadastra_historicos_vacinacao, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
