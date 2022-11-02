# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

num1 = int(input('Insira o primeiro número: '))

print('O número antecessor ao número {} é o {} e o sucessor é o {}.'.format(num1, num1-1, num1+1))