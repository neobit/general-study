# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


reta1 = int(input('Digite o tamanho da primeira reta: '))
reta2 = int(input('Digite o tamanho da segunda reta: '))
reta3 = int(input('Digite o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[0;30;42mÉ um triangulo!\033[m')
else:
    print('Não é um triangulo.')