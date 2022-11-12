# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior o segundo valor é maior não existe valor maior os dois são iguais

num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior ({}). O segundo valor é o menor ({}).'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor é maior ({}). O primeiro valor é o menor ({}).'.format(num2, num1))
else:
    print('Não há valor menor ou maior, os dois são iguais.')