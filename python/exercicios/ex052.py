# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuári odigitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

numbers = []
Program = True
soma = 0
inputed = 0

while Program == True:
    inputed = input('Digite um número inteiro [Digite Parar para interromper]: ').upper()
    if inputed == 'PARAR':
        print('Finalizando programa.')
        Program = False
    else:
        numbers.append(int(inputed))


lenghtnumbers = len(numbers)

counter = 0
while counter < lenghtnumbers:
    soma += numbers[counter]
    counter += 1

print('Foram digitados {} números. A soma entre todos eles é de: {}'.format(len(numbers), soma))
