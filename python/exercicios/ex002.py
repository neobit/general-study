# Exercício: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

userInput = input('Digite alguma palavra ou número: ')

print('O tipo primitivo do dado inserido é: {}'.format(type(userInput)))
print('Ele só tem espaços?: {}'.format(userInput.isspace())) # Função .isspace testa se há apenas espaço no valor referido.
print('É um número?: {}'.format(userInput.isnumeric()))
print('É alfabético?: {}'.format(userInput.isalpha()))
print('É alfanumérico?: {}'.format(userInput.isalnum()))
print('Está em maiusculo?: {}'.format(userInput.isupper()))
print('Está em minusculo?: {}'.format(userInput.islower()))
print('Está capitalizado?: {}'.format(userInput.istitle()))