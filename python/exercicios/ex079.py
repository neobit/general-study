# Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint as random
from time import sleep as cooldown

numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        choosednumber = random(0, 99)
        print(choosednumber, end=' ')
        cooldown(0.5)
        numeros.append(choosednumber)
    print('PRONTO!')

def somaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma = soma + i
    print(f'Somando os valores pares de {numeros}, temos: {soma}')

sorteia()
somaPar()