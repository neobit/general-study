# Faça um programa que tenha uma funcao chamada contador(), que receba tres parametros: inicio, fim e passo e realize a contagem. 
# Seu programa tem que realizar tres contagens atraves da funcao criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.

from time import sleep as cooldown
def lin():
    print('-='*20)

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo * -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
            cooldown(0.1)
    else:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ')
            cooldown(0.1)
    print('FIM!')
    lin()

lin()
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
