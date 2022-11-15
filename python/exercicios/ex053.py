# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numbers = []
_program = True
inputed = 0
opt = ''

while _program == True:
    inputed = input('Digite um número inteiro [Digite PARAR para interromper]: ').upper()
    if inputed == 'PARAR':
        _program = False
    else:
        numbers.append(int(inputed))
    opt = input('Deseja adicionar mais um valor? [S/N]: ')
    if opt == 'N':
        _program = False
    
counter = 0
media = 0
maior = 0
menor = 999
while counter < len(numbers):
    media += numbers[counter]
    if numbers[counter] > maior:
        maior = numbers[counter]
    elif numbers[counter] < menor:
        menor = numbers[counter]
    counter += 1
media = media / len(numbers)

print('A média entre todos os valores digitados é {:.2f}. O maior número digitado é o {} e o menor é o {}.'.format(media, maior, menor))