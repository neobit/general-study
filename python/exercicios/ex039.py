# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

firsterm = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

for i in range(firsterm,(firsterm + (10 - 1)*razao)+1, razao):
    print(i, end=' -> ')
print('Acabou')
