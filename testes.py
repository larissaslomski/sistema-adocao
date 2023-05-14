class TipoHabitacao:
    def __init__(self, tipo_hab: str, tamanho_hab: str):
        self.__tipo_hab = tipo_hab
        self.__tamanho_hab = tamanho_hab

    def __str__(self):
        return f"Tipo: {self.__tipo_hab}, Tamanho: {self.__tamanho_hab}"


tipo_habitacao = TipoHabitacao("Casa", "Grande")
print(tipo_habitacao)


""" from random import randint
result = []
r = randint(100, 999)
if r not in result:
    result.append(r)

print(result) """
