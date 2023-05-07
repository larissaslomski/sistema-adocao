class TelaTipoHabitacao():
    def tela_opcoes(self):
        print("------- TIPO HABITAÇÃO --------")
        print("Escolha a opcao")
        print("1 - Casa pequena")
        print("2 - Casa média")
        print("3 - Casa grande")
        print("4 - Apartamento pequeno")
        print("5 - Apartamento médio")
        print("6 - Apartamento grande")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostrar_mensagem(self, mensagem):
        return mensagem

    # def mostra_tipo_habitacao(self, dados_gato):
    #     print("NUMERO CHIP DO GATO: ", dados_gato["numero chip"])
    #     print("NOME DO GATO: ", dados_gato["nome"])
    #     print("RAÇA DO GATO: ", dados_gato["raca"])
    #     print("\n")