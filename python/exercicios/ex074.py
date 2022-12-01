jogador = dict()
jogadores = list()
cont = ''
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    gols = list()
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols foram realizados na partida {i+1}?: ')))
        jogador['gols'] = gols[:]
        jogador['total'] = 0
        for i in gols:
            jogador['total'] = jogador['total'] + i
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = input('Quer continuar? [S/N]: ').upper()
    if cont == 'N':
        break

print('-='*30)
print(f'{"cod.":<4}{"nome":<10}{"gols":>8}{"total":>8}')
print('-'*30)
for i in range(0, len(jogadores)):
    print('{0} {1} {2} {3}'.format(i, jogadores[i]['nome'], jogadores[i]['gols'], jogadores[i]['total']))
cond = 0
while True:
    print('-'*30)
    cond = int(input('Mostrar dado de qual jogador?: '))
    if cond == 999:
        break
    elif cond >= len(jogadores):
        print(f'Erro! Não existe jogador com código {cond}.')
    else:
        print('Levantamento do jogador {}:'.format(jogadores[cond]['nome']))
        for i in range(0, len(jogadores[cond]['gols'])):
            print('No jogo {0} fez {1} gols.'.format(i+1, jogadores[cond]['gols'][i]))