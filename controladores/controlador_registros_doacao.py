from entidades.registro_doacao import RegistroDoacao
from telas.tela_registro_doacao import TelaRegistroDoacao
from uuid import uuid4
from datetime import date


class ControladorRegistrosDoacao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__registros_doacao = []
        self.__tela_registro_doacao = TelaRegistroDoacao()

    def verifica_animal_doado(self):
        for registro_doacao in self.__registros_doacao:
            if registro_doacao

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
            self.__controlador_sistema.controlador_cachorros.incluir_cachorro()
            self.__controlador_sistema.controlador_doadores.incluir_doador()
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
        elif cachorro_ou_gato == 2:
            self.__controlador_sistema.controlador_gatos.incluir_gato()
            self.__controlador_sistema.controlador_doadores.incluir_doador()
            self.__controlador_sistema.controlador_gatos.listar_gatos()
            self.__controlador_sistema.controlador_doadores.listar_doadores()
            self.__tela_registro_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do gato e o motivo da doação:")
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
                    f"Inclusão de registro de doação realizada com sucesso.")
            else:
                self.__tela_registro_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente.")

    def listar_registro_doacao(self):
        for registro_doacao in self.__registros_doacao:
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

    def gerar_relatorio_doacao(self):
        data_inicial = self.__tela_registro_doacao.pega_datas_relatorio(
            "Data Inicial")
        data_final = self.__tela_registro_doacao.pega_datas_relatorio(
            "Data Final")
        cont = 0
        for registro in self.__registros_doacao:
            if registro.data > data_inicial and registro.data < data_final:
                cont += 1
        self.__tela_registro_doacao.mostra_mensagem(
            f"Entre {data_inicial} e {data_final} foram adotados {cont} animais.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_registro_doacao, 2: self.listar_registro_doacao, 3: self.excluir_registro_doacao, 
                        4: self.gerar_relatorio_doacao, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_registro_doacao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_registro_doacao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_registro_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
