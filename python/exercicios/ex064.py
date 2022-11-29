# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dataInputed = list()
pessoas = list()
minkg = 999
maxkg = 0
peoplefat = []
peopleskinny = []
qnt = int(input('Digite quantas pessoas deseja inserir: '))
for i in range(0, qnt):
    dataInputed.append(str(input('Digite o nome da pessoa: ')))
    dataInputed.append(float(input('Digite o peso da pessoa em quilogramas: ')))
    if dataInputed[1] < minkg:
        minkg = dataInputed[1]
        #print(f'O peso do {dataInputed[1]} entrou na minkg.')
    if dataInputed[1] > maxkg:
        maxkg = dataInputed[1]
        #print(f'O peso do {dataInputed[1]} entrou na maxkg.')
    pessoas.append(dataInputed[:])
    dataInputed.clear()


for i in pessoas:
    if i[1] == minkg:
        peopleskinny.append(i[0])
    if i[1] == maxkg:
        peoplefat.append(i[0])

print(f'Ao todo, você cadastrou {qnt} pessoas.')
print(f'O maior peso foi de {maxkg}kg. Peso de: {peoplefat}')
print(f'O menor peso foi de {minkg}kg. Peso de: {peopleskinny}')
