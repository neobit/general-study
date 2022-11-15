# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá leu um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    opt = int(input('Digite um número entre 0 e 20: '))
    if opt > 20 or opt < 0:
        print('Tente novamente.', end=' ')
    elif opt > -1 and opt < 21:
        break

print(f'Você digitou o número {numbers[opt]}')