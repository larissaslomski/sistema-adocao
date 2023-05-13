from entidades.animal import Animal
from entidades.historico_vacinacao import HistoricoVacinacao


class Gato(Animal):
    #incluir historico de vacinacao no init e super(classe super tmb)

    def __init__(self, numero_chip: int, nome: str, raca: str):
        super().__init__(numero_chip, nome, raca)
