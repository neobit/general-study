# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

num = []
for i in range(0,6):
    num.append(int(input('Digite {}º que você quer: '.format(i+1))))

soma = 0
for i in range(0,len(num)):
    soma = soma + num[i]

print('A soma final de todos os valores é: {}'.format(soma))