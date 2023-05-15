from entidades.historico_vacinacao import HistoricoVacinacao
from telas.tela_historico_vacinacao import TelaHistoricoVacinacao
from uuid import uuid4
from datetime import date


class ControladorHistoricoVacinacao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__historicos_vacinacao = []
        self.__tela_historico_vacinacao = TelaHistoricoVacinacao()

    # def pega_registro_adocao_por_codigo(self, codigo: int):
    #     for registro_adocao in self.__registros_adocao:
    #         if registro_adocao.codigo_registro == codigo:
    #             return registro_adocao
    #     return None

    def incluir_historico_vacinacao(self):
        cachorro_ou_gato = self.__tela_historico_vacinacao.seleciona_cachorro_ou_gato()
        while True:
            if cachorro_ou_gato not in (1, 2):
                self.__tela_historico_vacinacao.mostra_mensagem(
                    "Opção inválida! Selecione 1 ou 2!")
                cachorro_ou_gato = self.__tela_historico_vacinacao.seleciona_cachorro_ou_gato()
            else:
                break
        if cachorro_ou_gato == 1:
            self.__controlador_sistema.controlador_vacinas.incluir_vacina()
            self.__controlador_sistema.controlador_cachorros.listar_cachorros()
            self.__controlador_sistema.controlador_vacinas.listar_vacina()
            dados_historico_vacinacao = self.__tela_historico_vacinacao.pega_dados_historico()
            cachorro = self.__controlador_sistema.controlador_cachorros.pega_cachorro_por_num_chip(
                dados_historico_vacinacao["numero_chip_animal"])
            vacina = self.__controlador_sistema.controlador_vacinas.incluir_vacina()
            if cachorro is not None and vacina is not None:
                data = date.today()
                historico_vacinacao = HistoricoVacinacao(
                    data, cachorro, vacina)
                cachorro.historicos_vacinacao.append(historico_vacinacao)
            else:
                self.__tela_historico_vacinacao.mostra_mensagem(f"Não há nenhum cachorro cadastrado com numero chip: "
                                                                f"{dados_historico_vacinacao['numero_chip_animal']} para vacinar")
        if cachorro_ou_gato == 2:
            self.__controlador_sistema.controlador_vacinas.incluir_vacina()
            self.__controlador_sistema.controlador_gatos.listar_gatos()
            self.__controlador_sistema.controlador_vacinas.listar_vacina()
            dados_historico_vacinacao = self.__tela_historico_vacinacao.pega_dados_historico()
            vacina = self.__controlador_sistema.controlador_vacinas.pega_vacina_por_nome(
                dados_historico_vacinacao["nome_vacina"])
            gato = self.__controlador_sistema.controlador_gatos.pega_gato_por_num_chip(
                dados_historico_vacinacao["numero_chip_animal"])
            if gato is not None and vacina is not None:
                data = date.today()
                historico_vacinacao = HistoricoVacinacao(data, gato, vacina)
                gato.historicos_vacinacao.append(historico_vacinacao)
            else:
                self.__tela_historico_vacinacao.mostra_mensagem(f"Não há nenhum gato cadastrado com numero chip: "
                                                                f"{dados_historico_vacinacao['numero_chip_animal']} para vacinar")

    def listar_historico_vacinacao(self):
        for historico_vacinacao in self.__historicos_vacinacao:
            # fazer metodo abstrato para mostrar animal
            self.__tela_historico_vacinacao.mostra_historico_vacinacao({"data": historico_vacinacao.data,
                                                                        "vacina": historico_vacinacao.vacina.nome_vacina})

    def excluir_historico_vacinacao(self):
        pass
        # self.listar_historico_vacinacao()
        # codigo_registro_adocao = self.__tela_registro_adocao.seleciona_registro_adocao()
        # registro_adocao = self.pega_registro_adocao_por_codigo(int(codigo_registro_adocao))
        #
        # if registro_adocao is not None:
        #     self.__registros_adocao.remove(registro_adocao)
        #     self.__tela_registro_adocao.mostra_mensagem(f"Registro de adoção com código {codigo_registro_adocao} removido com sucesso.")
        #     self.listar_registro_adocao()
        # else:
        #     self.__tela_registro_adocao.mostra_mensagem("ATENCAO: Codigo de registro não existente")

    def alterar_registro_adocao(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_historico_vacinacao(), 2: self.listar_historico_vacinacao(), 3: self.alterar_registro_adocao(), 4: self.excluir_historico_vacinacao(),
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_historico_vacinacao.tela_opcoes()]()
