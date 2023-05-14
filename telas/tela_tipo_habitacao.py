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

    def mostrar_mensagem(self, msg):
        print(msg)
