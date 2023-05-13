from entidades.registro_adocao import RegistroAdocao
from telas.tela_registro_adocao import TelaRegistroAdocao


class ControladorRegistrosAdocao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__registros_adocao = []
        self.__tela_registro_adocao = TelaRegistroAdocao()

    def pega_registro_adocao_por_codigo(self, codigo: int):
        for registro_adocao in self.__registros_adocao:
            if registro_adocao.codigo_registro == codigo:
                return registro_adocao
        return None

    def incluir_registro_adocao(self):
        self.__controlador_sistema.controlador_adotantes.listar_adotantes()
        self.__controlador_sistema.controlador_cachorros.listar_cachorros()
        self.__controlador_sistema.controlador_gatos.listar_gatos()
        dados_registro_adocao = self.__tela_registro_adocao.pega_dados_registro_adocao()

        adotante = self.__controlador_sistema.controlador_adotantes.pega_adotante_por_cpf(dados_registro_adocao["cpf"])
        cachorro = self.__controlador_sistema.controlador_cachorros.pega_cachorro_por_num_chip(dados_registro_adocao["codigo"])
        if (amigo is not None and livro is not None):
            emprestimo = Emprestimo(amigo, livro, randint(0, 100))
            self.__emprestimos.append(emprestimo)
        else:
            self.__tela_emprestimo.mostra_mensagem("Dados invalidos")