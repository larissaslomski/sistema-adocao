from entidades.gato import Gato
from telas.tela_gato import TelaGato


class ControladorGatos():
    def __init__(self, controlador_sistema):
        self.__gatos = []
        self.__tela_gato = TelaGato()
        self.__controlador_sistema = controlador_sistema

    def pega_gato_por_num_chip(self, num_chip: int):
        for gato in self.__gatos:
            if (gato.num_chip == num_chip):
                return gato
        return None

    def incluir_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
        num_chip_valido = self.pega_gato_por_num_chip(
            dados_gato['num_chip'])
        if num_chip_valido is None:
            gato = gato(dados_gato["num_chip"], dados_gato["nome"], dados_gato["raca"],
                        dados_gato["historico_vacinacao"])
            self.__gatos.append(gato)
            self.__tela_gato.mostra_mensagem(
                "Animal cadastrado com sucesso no Sistema.")
        else:
            self.__tela_gato.mostra_mensagem(
                "ERRO: o Animal ja esta cadastrado no Sistema.")

    def listar_gatos(self):
        tam_lista_gatos = len(self.__gatos)
        if tam_lista_gatos > 0:
            for gato in self.__gatos:
                self.__tela_gato.mostra_gato(
                    {"num_chip": gato.num_chip, "nome": gato.nome, "raca": gato.raca})
                    # como listar historicos? apenas no controlador de historicos?
        else:
            self.__tela_gato.mostra_mensagem(
                "ERRO: Não existe nenhum Gato cadastrado no Sistema.")

    def alterar_gato(self):
        self.listar_gatos()
        num_chip = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_num_chip(num_chip)

        if (gato is not None):
            novos_dados_gato = self.__tela_gato.pega_dados_gato()
            gato.nome = novos_dados_gato["nome"]
            gato.raca = novos_dados_gato["raca"]
            # num_chip é fixo (?)
            # historico_vacinacao só pode ser alterado na sua tela (?)
            self.listar_gatos()
        else:
            self.__tela_gato.mostra_mensagem(
                "ERRO: O gato não existe.")

    def excluir_gato(self):
        self.listar_gatos()
        num_chip = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_num_chip(num_chip)

        if (gato is not None):
            self.__gatos.romove(gato)
            self.listar_gatos()
        else:
            self.__tela_gato.mostra_mensagem(
                "ERRO: O gato não existe.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_gato, 2: self.alterar_gato,
                        3: self.listar_gatos, 4: self.excluir_gato, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_gato.tela_opcoes()]()
