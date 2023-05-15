class TelaHistoricoVacinacao():
    def tela_opcoes(self):
        print("-------- HISTÓRICO VACINAÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir histórico de vacinação")
        print("2 - Listar históricos de vacinação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_cachorro_ou_gato(self):
        print("Um cachorro um gato será vacinado?")
        print("1 - Cachorro")
        print("2 - Gato")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_historico(self):
        print("-------- HISTÓRICO VACINAÇÃO --------")
        numero_chip_animal = int(
            input("Digite o número do chip do animal vacinado: "))
        return {"numero_chip_animal": numero_chip_animal}

    def mostra_historico_vacinacao(self, dados_historico_vacinacao):
        print("DATA VACINACAO: ", dados_historico_vacinacao["data"])
        print("ANIMAL: ", dados_historico_vacinacao["animal"])
        print("NOME DA VACINA: ", dados_historico_vacinacao["vacina"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)
