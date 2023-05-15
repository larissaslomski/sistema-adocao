from entidades.registro_doacao import RegistroDoacao
from telas.tela_registro_doacao import TelaRegistroDoacao
from uuid import uuid4
from datetime import date


class ControladorRegistrosDoacao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__registros_doacao = []
        self.__tela_registro_doacao = TelaRegistroDoacao()

    def pega_registro_doacao_por_codigo(self, codigo: int):
        for registro_doacao in self.__registros_doacao:
            if registro_doacao.codigo_registro == codigo:
                return registro_doacao
        return None

    def pega_registro_doacao_por_doador(self, doador):
        for registro_doacao in self.__registros_doacao:
            if registro_doacao.doador.cpf == doador.cpf:
                return registro_doacao
        return None

    def relatorio_doacao_periodo(self):
        data_inicial = self.__tela_registro_doacao.pega_datas_relatorio(
            "Data Inicial")
        data_final = self.__tela_registro_doacao.pega_datas_relatorio(
            "Data Final")
        for registro in self.__registros_doacao:
            if registro.data > data_inicial and registro.data < data_final:
                cont = cont + 1
        self.__tela_registro_doacao.mostra_mensagem(
            f"Entre {data_inicial} e {data_final} foram doados {cont} animais.")

    def incluir_registro_doacao(self):
        cachorro_ou_gato = self.__tela_registro_doacao.seleciona_cachorro_ou_gato()
        while True:
            if cachorro_ou_gato not in (1, 2):
                self.__tela_registro_doacao.mostra_mensagem(
                    "Opção inválida! Selecione 1 ou 2!")
                cachorro_ou_gato = self.__tela_registro_doacao.seleciona_cachorro_ou_gato()
            else:
                break
        if cachorro_ou_gato == 1:
            self.__controlador_sistema.controlador_cachorros.listar_cachorros()
            self.__controlador_sistema.controlador_doadores.listar_doadores()
            self.__tela_registro_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do cachorro e o motivo da doação:")
            dados_registro_doacao = self.__tela_registro_doacao.pega_dados_registro_doacao()
            doador = self.__controlador_sistema.controlador_doadores.pegar_doador_por_cpf(
                dados_registro_doacao["cpf"])
            cachorro = self.__controlador_sistema.controlador_cachorros.pega_cachorro_por_num_chip(
                dados_registro_doacao["numero_chip"])
            if doador is not None and cachorro is not None:
                codigo_registro = uuid4().int
                data = date.today()
                registro_doacao = RegistroDoacao(
                    codigo_registro, data, cachorro, doador, dados_registro_doacao["motivo"])
                self.__registros_doacao.append(registro_doacao)
                self.__tela_registro_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso!")
            else:
                self.__tela_registro_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente.")
                # fazer while verificação
        elif cachorro_ou_gato == 2:
            self.__tela_registro_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do gato e o motivo da doação:")
            self.__controlador_sistema.controlador_gatos.listar_gatos()
            self.__controlador_sistema.controlador_doadores.listar_doadores()
            dados_registro_doacao = self.__tela_registro_doacao.pega_dados_registro_doacao()
            motivo = dados_registro_doacao["motivo"]
            doador = self.__controlador_sistema.controlador_doadores.pegar_doador_por_cpf(
                dados_registro_doacao["cpf"])
            gato = self.__controlador_sistema.controlador_gatos.pega_gato_por_num_chip(
                dados_registro_doacao["numero_chip"])
            if doador is not None and gato is not None:
                codigo_registro = uuid4().int
                data = date.today()
                registro_doacao = RegistroDoacao(
                    codigo_registro, data, gato, doador, motivo)
                self.__registros_doacao.append(registro_doacao)
                self.__tela_registro_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso")
            else:
                self.__tela_registro_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente.")
                # fazer while verificação

    def listar_registro_doacao(self):
        for registro_doacao in self.__registros_doacao:
            # inserir animalfazer metodo abstrato em animal
            self.__tela_registro_doacao.mostra_registro_doacao({"codigo_registro": registro_doacao.codigo_registro,
                                                                "data": registro_doacao.data,
                                                                "nome_doador": registro_doacao.doador.cpf,
                                                                "motivo": registro_doacao.motivo})

    def excluir_registro_doacao(self):
        self.listar_registro_doacao()
        codigo_registro_doacao = self.__tela_registro_doacao.seleciona_registro_doacao()
        registro_doacao = self.pega_registro_doacao_por_codigo(
            int(codigo_registro_doacao))

        if registro_doacao is not None:
            self.__registros_doacao.remove(registro_doacao)
            self.__tela_registro_doacao.mostra_mensagem(
                f"Registro de doação com código {codigo_registro_doacao} removido com sucesso.")
            self.listar_registro_doacao()
        else:
            self.__tela_registro_doacao.mostra_mensagem(
                "ATENCAO: Codigo de registro não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_registro_doacao, 2: self.listar_registro_doacao, 3: self.excluir_registro_doacao,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_registro_doacao.tela_opcoes()]()
