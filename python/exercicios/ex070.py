# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint as random
from time import sleep as cooldown

players = dict()
position = list()

for i in range(0, 4):
    players[i] = random(1,6)
    print(f'O jogador {i+1} tirou {players[i]}.')
    cooldown(1)

position.append
for i in players:
    position.append