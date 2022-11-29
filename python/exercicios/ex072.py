# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

gols = list()
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols foram realizados na partida {i+1}?: ')))
jogador['gols'] = gols[:]
print('-='*30)
print(jogador)
print('-='*30)
for x, y in jogador:
    print(f'O campo {x} tem o valor {y}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0, jogador['partidas']):
    print(f' => Na partida {i+1}, fez {jogador[]} gols.')