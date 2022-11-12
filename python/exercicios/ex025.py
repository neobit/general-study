# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - Binário 2 - Octal 3 - Hexadecimal

num = int(input('Informe um número inteiro para realizar uma conversão desse número: '))
opt = int(input('''Escolha uma das opções para realizar a conversão:
1.Converter para Binário
2.Converter para Octal
3.Converter para Hexadecimal
Digite a opção desejada: '''))

if opt == 1:
    print('O seu número convertido em binário é: {}'.format(bin(num).replace('0b','')))
elif opt == 2:
    print('O seu número convertido em octal é: {}'.format(oct(num)[2:]))
elif opt == 3:
    print('O seu número convertido em octal é: {}'.format(hex(num)[2:]))
else:
    print('Opção inválida.')