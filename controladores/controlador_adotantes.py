from entidades.adotante import Adotante
from telas.tela_adotante import TelaAdotante


class ControladorAdotantes:
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()
        self.__controlador_sistema = controlador_sistema

    def pega_adotante_por_cpf(self, cpf: int):
        for adotante in self.__adotantes:
            if (adotante.cpf == cpf):
                return adotante
        return None

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        cpf_valido = self.pega_adotante_por_cpf(dados_adotante['cpf'])
        if cpf_valido is None:
            tem_outros_animais = dados_adotante["tem_outros_animais"]
            if tem_outros_animais.upper() == "S" or tem_outros_animais.upper() == "N":
                adotante = Adotante(
                dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["nascimento"], dados_adotante["endereco"], dados_adotante["tem_outros_animais"])
                self.__adotantes.append(adotante)
                self.__tela_adotante.mostra_mensagem("Adotante cadastrado com sucesso no sistema")
            else:
                self.__tela_adotante.mostra_mensagem("ERRO: informações inválidas, tente novamente")
                self.__tela_adotante.pega_dados_adotante()
        else:
            self.__tela_adotante.mostra_mensagem("ERRO: o Adotante ja esta cadastrado no Sistema.")


    def listar_adotantes(self):
        tam_lista_adotantes = len(self.__adotantes)
        if tam_lista_adotantes > 0:
            for adotante in self.__adotantes:
                self.__tela_adotante.mostra_adotante(
                    {"cpf": adotante.cpf, "nome": adotante.nome, "nascimento": adotante.nascimento, "tipo_habitacao": adotante.tipo_habitacao})
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: Não existe nenhum adotante cadastrado no Sistema.")

    def alterar_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pegar_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"]
            adotante.nascimento = novos_dados_adotante["nascimento"]
            # conferir se as instancias de tipo_habitacao esta corretas
            adotante.tipo_habitacao.tipo_hab = novos_dados_adotante["tipo_hab"]
            adotante.tipo_habitacao.tamanho_hab = novos_dados_adotante["tamanho_hab"]
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante não existe.")

    def excluir_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pegar_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            self.__adotantes.romove(adotante)
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante não existe.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adotante, 2: self.alterar_adotante,
                        3: self.listar_adotantes, 4: self.excluir_adotante, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_adotante.tela_opcoes()]()
