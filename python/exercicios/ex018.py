# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Informe um número: '))
res = num % 2

if res == 0:
    print('O número que você informou é PAR!')
else:
    print('O número que você informou é ÍMPAR')