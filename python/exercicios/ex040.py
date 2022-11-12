# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro para verificar se é um número primo: '))
mult = 0

for i in range (2, num):
    if num % i == 0:
        mult += 1

if mult == 0 and num != 1:
    print('É primo.')
else:
    print('Não é primo.')