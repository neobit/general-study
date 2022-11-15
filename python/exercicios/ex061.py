# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numbers = []
while True:
    inputed = int(input('Digite um valor: '))
    numbers.append(inputed)
    opt = input('Quer continuar? [S/N]: ').upper()
    if opt == 'N':
        break

numbers.sort(reverse=True)
print(f'Foram digitados {len(numbers)} números. Os números digitados foram: {numbers}')
if 5 in numbers:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')