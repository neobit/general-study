# Faça um programa que tenha uma função chamada maior(), que recebe vários parametros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep as cooldown

def maior(*numbers):
    print('-='*30)
    print('Analisando os valores passados...')
    mayor = 0
    tam = len(numbers)
    for i in numbers:
        cooldown(0.5)
        print(i, end=' ')
        if i > mayor:
            mayor = i
    if tam > 0:
        print(f'| Foram informados {tam} valores ao todo.')
    else:
        print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor indormado foi {mayor}')

maior(2,9,4,5,6,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()