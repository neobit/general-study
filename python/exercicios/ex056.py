# Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint as random

maior = 0
menor = 999
numbers = (random(0,999), random(0,999), random(0,999), random(0,999), random(0,999))

print(f'Os valores sorteador foram: ', end='')
for i in numbers:
    print(i, end=' ')

print(f'\nO maior valor sorteador foi: {max(numbers)}')
print(f'O menor valor sorteador foi: {min(numbers)}')
