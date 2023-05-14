class TelaVacina():
    def tela_opcoes(self):
        print("------- VACINA --------")
        print("Escolha a opcao")
        print("1 - Incluir vacina")
        print("2 - Alterar vacina")
        print("3 - Listar vacinas")
        print("4 - Excluir vacina")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_vacina_nome(self):
        print("-------- DADOS VACINA ----------")
        nome_vacina = input("Nome vacina: ")
        return {"nome_vacina": nome_vacina}

    def mostra_vacina(self, dados_vacina):
        print("NOME DA VACINA: ", dados_vacina["nome_vacina"])
        print("\n")

    def seleciona_vacina(self):
        numero_chip = int(input("Nome da vacina que deseja selecionar: "))
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)