from entidades.cachorro import Cachorro
from telas.tela_cachorro import TelaCachorro
from uuid import uuid4


class ControladorCachorros:
    def __init__(self, controlador_sistema):
        self.__cachorros = []
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistema = controlador_sistema

    def pega_cachorro_por_num_chip(self, num_chip: int):
        for cachorro in self.__cachorros:
            if (cachorro.num_chip == num_chip):
                return cachorro
        return None

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        numero_chip = uuid4().int
        tamanho = self.__tela_cachorro.tamanho_cachorro()
        while True:
            if tamanho.upper() not in ('P', 'M', 'G'):
                self.__tela_cachorro.mostra_mensagem("Informação inválida, selecione P, M ou G")
                tamanho = self.__tela_cachorro.tamanho_cachorro()
            else:
                break
        dados_cachorro["tamanho"] = tamanho.upper()
        cachorro = Cachorro(numero_chip, dados_cachorro["nome"], dados_cachorro["raca"], dados_cachorro["tamanho"])
        dados_cachorro["numero_chip"] = numero_chip
        self.__cachorros.append(cachorro)
        self.__tela_cachorro.mostra_mensagem(
            "Animal cadastrado com sucesso no Sistema.")
        # else:
        #     self.__tela_cachorro.mostra_mensagem(
        #         "ERRO: o Animal ja esta cadastrado no Sistema.")

    def listar_cachorros(self):
        tam_lista_cachorros = len(self.__cachorros)
        if tam_lista_cachorros > 0:
            for cachorro in self.__cachorros:
                self.__tela_cachorro.mostra_cachorro(
                    {"numero_chip": cachorro.num_chip, "nome": cachorro.nome, "raca": cachorro.raca, "tamanho": cachorro.tamanho, "historico": cachorro.listar_vacinas_historico()})

        else:
            self.__tela_cachorro.mostra_mensagem(
                "ERRO: Não existe nenhum cachorro cadastrado no Sistema.")
            self.__controlador_sistema.abre_tela()

    def alterar_cachorro(self):
        self.listar_cachorros()
        num_chip = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_num_chip(num_chip)

        if (cachorro is not None):
            novos_dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
            tamanho = self.__tela_cachorro.tamanho_cachorro()
            while True:
                if tamanho.upper() not in ('P', 'M', 'G'):
                    self.__tela_cachorro.mostra_mensagem("Informação inválida, selecione P, M ou G")
                    tamanho = self.__tela_cachorro.tamanho_cachorro()
                else:
                    break
            novos_dados_cachorro["tamanho"] = tamanho.upper()
            cachorro.nome = novos_dados_cachorro["nome"]
            cachorro.raca = novos_dados_cachorro["raca"]
            cachorro.tamanho = novos_dados_cachorro["tamanho"]
            # num_chip é fixo (?) resposta: vou considerar q sim
            # historico_vacinacao só pode ser alterado na sua tela (?)
            self.__tela_cachorro.mostra_mensagem("Dados do cachorro alterados com sucesso.")
            # self.listar_cachorros()
        else:
            self.__tela_cachorro.mostra_mensagem(
                "ERRO: O cachorro não existe.")
            self.__tela_cachorro.tela_opcoes()

    def excluir_cachorro(self):
        self.listar_cachorros()
        num_chip = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_num_chip(num_chip)

        if (cachorro is not None):
            self.__cachorros.remove(cachorro)
            self.__tela_cachorro.mostra_mensagem(
                f"O cachorro de numero chip: {num_chip} foi excluido do sistema")
            if len(self.__cachorros) == 0:
                self.__tela_cachorro.mostra_mensagem(
                    "Não existe mais nenhum cachorro cadastrado no sistema")
            else:
                self.__tela_cachorro.tela_opcoes()
        else:
            self.__tela_cachorro.mostra_mensagem(
                "ERRO: O Cachorro não existe.")
            self.__tela_cachorro.tela_opcoes()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cachorro, 2: self.alterar_cachorro,
                        3: self.listar_cachorros, 4: self.excluir_cachorro, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cachorro.tela_opcoes()]()
