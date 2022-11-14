# Faça um programa que leia um número qualquer e mostre o seu fatorial.

inputed = int(input('Digite um número para saber seu fatorial: '))

counter = 1
fatorial = inputed
while counter != inputed:
    fatorial = fatorial * (inputed - counter)
    counter += 1

print('O fatorial de {}! é {}.'.format(inputed, fatorial))