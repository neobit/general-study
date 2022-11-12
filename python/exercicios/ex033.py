# Crie um programa que faça o computador jogar Jokenpô com você.
import random

print('\033[0;31;40m')
print('==-=='*20)
print('\n\n\n Vamos jogar Jokenpô? hehehehehe.\n\n\n')
print('==-=='*20)
print('\033[m')

opt = (input('Digite PEDRA, PAPEL ou TESOURA: ')).upper()
cpuchoose = (random.choice(['PEDRA','PAPEL','TESOURA'])).upper()

print('Eu escolhi {}.'.format(cpuchoose))

if cpuchoose == opt:
    print('Puts!! Empatamos!!')
else:
    if cpuchoose == 'PEDRA':
        if opt == 'PAPEL':
            print('Puts!! Você Ganhou!!')
        elif opt == 'TESOURA':
            print('HAHAHAHA!! EU GANHEI!!')
    elif cpuchoose == 'PAPEL':
        if opt == 'TESOURA':
            print('Puts!! Você Ganhou!!')
        elif opt == 'PEDRA':
            print('HAHAHAHA!! EU GANHEI!!')
    elif cpuchoose == 'TESOURA':
        if opt == 'PAPEL':
            print('HAHAHAHA!! EU GANHEI!!')
        elif opt == 'PEDRA':
            print('Puts!! Você Ganhou!!')