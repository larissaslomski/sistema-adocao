from datetime import date
class TelaRegistroDoacao():
    def tela_opcoes(self):
        print("-------REGISTRO DE DOAÇÃO--------")
        print("Escolha a opcao")
        print("1 - Incluir registro de doação")
        print("2 - Alterar registro de doação")
        print("3 - Listar registros de doação")
        print("4 - Excluir registro de doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_cachorro_ou_gato(self):
        print("Um cachorro um gato será doado?")
        print("1 - Cachorro")
        print("2 - Gato")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_registro_doacao(self):
        print("-------- DADOS REGISTRO DE DOAÇÃO ----------")
        cpf_doador = input("Cpf do doador: ")
        numero_chip_animal = int(input("Numero do chip do animal a ser doado: "))
        motivo = input("Motivo doação: ")
        return {"cpf": cpf_doador, "numero_chip": numero_chip_animal, "motivo": motivo}

    def mostra_registro_doacao(self, dados_registro_doacao):
        print("CÓDIGO DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["codigo_registro"])
        print("DATA DO REGISTRO DE DOAÇÃO: ", dados_registro_doacao["data"])
        print("NOME DO DOADOR: ", dados_registro_doacao["nome_doador"])
        print("MOTIVO DA DOAÇÃO: ", dados_registro_doacao["motivo"])
        print("\n")

    def seleciona_registro_doacao(self):
        registro = input("codigo do registro que deseja selecionar: ")
        return registro

    def mostra_mensagem(self, msg):
        print(msg)