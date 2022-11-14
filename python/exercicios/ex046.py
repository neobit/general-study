# Melhore o jogo de um dos seus primeiros desafios mas agora o computado vai pensar em um número entre 0 e 10. O jogador vai ter que tentar adivinhar até acertar, mostrando no final quantos palpites foram necessário para vencer.

from random import randint as choose

counter = 0
inputed = ''
palpite = -1

gamechoose = choose(0,10)
print(gamechoose)

print('\033[0;31;40m')
print('==-=='*20)
print('\n\n\n Vamos jogar um jogo? hehehehehe.\n\n\n')
print('Pensei em um número entre 0 e 10, tenta adivinhar qual é!')
print('==-=='*20)
print('\033[m')

while palpite != gamechoose:
    palpite = int(input('Qual é o seu palpite?: '))
    if palpite == gamechoose:
        if counter == 0:
            print('EITA PORRA, VOCÊ ACERTOU DE PRIMEIRA O_O')
        elif counter >= 8:
            print('Tu teve que basicamente chutar quase todos números pra acertar... Mas parabéns... pela insistência.')
        else:
            print('Hehe! Parabéns! Só levou {} tentativas'.format(counter))
    else:
        print('HAHAHAHA VOCÊ ERROU, TENTE NOVAMENTE!')
        counter += 1