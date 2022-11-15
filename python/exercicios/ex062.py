# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crei duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numbers = []
pares = []
impares = []

while True:
    inputed = int(input('Digite um valor: '))
    numbers.append(inputed)
    if inputed % 2 == 0:
        pares.append(inputed)
    else:
        impares.append(inputed)
    opt = input('Quer continuar? [S/N]: ').upper()
    if opt == 'N':
        break

print(f'Lista de números: {numbers}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números impares: {impares}')