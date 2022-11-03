# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange

numberchoosed = randrange(0, 5)
print('Pensei em um número entre 0 e 5! Tente adivinhar qual é!')

guessinput = int(input('Escreva qual número você acha que é:'))

if numberchoosed == guessinput:
    print('Você acertou! O número {} foi realmente o número que eu pensei!'.format(guessinput))
else:
    print('hahahahaha! Você errou, {} não era o número que eu havia pensado! Na verdade era o {}'.format(guessinput, numberchoosed))