class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SISTEMA ADOÇÃO DE ANIMAIS ---------")
        print("Escolha sua opcao")
        print("1 - Cadastra adotante")
        print("2 - Cadastra doador")
        print("3 - Cadastra cachorro")
        print("4 - Cadastra gato")
        print("5 - Cadastra registro de adoção")
        print("6 - Cadastra registro de doação")
        print("7 - Cadastra histórico de vacinação")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)
