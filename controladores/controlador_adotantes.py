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
            tem_outros_animais = dados_adotante["tem_outros_animais"].upper()
            if tem_outros_animais == "S" or tem_outros_animais == "N":
                if tem_outros_animais == "S":
                    tem_outros_animais = True
                else:
                    tem_outros_animais = False
                adotante = Adotante(
                dados_adotante["cpf"], dados_adotante["nome"], dados_adotante["nascimento"], dados_adotante["endereco"], tem_outros_animais)
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
                    {"cpf": adotante.cpf, "nome": adotante.nome, "nascimento": adotante.nascimento, "endereco": adotante.endereco, "tem_outros_animais": adotante.tem_outros_animais})
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: Não existe nenhum adotante cadastrado no Sistema.")

    def alterar_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nome = novos_dados_adotante["nome"]
            adotante.nascimento = novos_dados_adotante["nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            # adotante.tem_outros_animais = novos_dados_adotante["tem_outros_animais"]
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante não existe.")

    def excluir_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if (adotante is not None):
            self.__adotantes.remove(adotante)
            self.__tela_adotante.mostra_mensagem(
                f"Adotante de cpf: {cpf_adotante} foi excluido do sistema.")
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
