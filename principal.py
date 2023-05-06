from entidades import (adotante, animal, cachorro, doador, gato, historico_vacinacao, pessoa, registro_adocao,
                       registro_doacao, tipo_habitacao, vacina)
from datetime import date
doador1 = doador.Doador('01236988754', 'larissa', '15/12/1996', 'blabla')
print(doador1.nome)
registro_doacao_doador1 = registro_doacao.RegistroDoacao(123, doador1, 'é a kiara')
print(registro_doacao_doador1.motivo)