# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O número {} é o maior.'.format(num1))
    if num2 < num3:
        print('E o número {} é o menor.'.format(num2))
    else:
        print('E o número {} é o menor.'.format(num3))
elif num2 > num1 and num2 > num3:
    print('O número {} é o maior.'.format(num2))
    if num1 < num3:
        print('E o número {} é o menor.'.format(num1))
    else:
        print('E o número {} é o menor.'.format(num3))
else:
    print('O número {} é o maior.'.format(num3))
    if num1 < num2:
        print('E o número {} é o menor.'.format(num1))
    else:
        print('E o número {} é o menor.'.format(num2))