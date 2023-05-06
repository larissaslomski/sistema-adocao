class TelaGato():
    def tela_opcoes(self):
        print("-------GATO --------")
        print("Escolha a opcao")
        print("1 - Incluir gato")
        print("2 - Alterar gato")
        print("3 - Listar gatos")
        print("4 - Excluir gato")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_gato(self):
        print("-------- DADOS GATO ----------")
        numero_chip = input("numero do chip: ")
        nome = input("Nome: ")
        raca = input("Raça: ")
        return {"numero chip": numero_chip, "nome": nome, "raca": raca}

    def mostra_gato(self, dados_gato):
        print("NUMERO CHIP DO GATO: ", dados_gato["numero chip"])
        print("NOME DO GATO: ", dados_gato["nome"])
        print("RAÇA DO GATO: ", dados_gato["raca"])
        print("\n")

    def seleciona_gato(self):
        numero_chip = input("Numero do chip do gato que deseja selecionar: ")
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
