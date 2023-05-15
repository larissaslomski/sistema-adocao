class TelaSistema:
    def tela_opcoes(self):
        print("-------- SISTEMA ADOÇÃO DE ANIMAIS --------")
        print("Escolha sua opção")
        print("1 - Menu adotante")
        print("2 - Menu doador")
        print("3 - Menu cachorro")
        print("4 - Menu gato")
        print("5 - Menu registro de adoção")
        print("6 - Menu registro de doação")
        print("7 - Menu histórico de vacinação")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)
