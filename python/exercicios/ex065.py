# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numlist = [[],[]]
pares = []
impares = []
inputed = 0
for i in range(0,7):
    inputed = int(input(f'Digite o {i}º número: '))
    if inputed % 2 == 0:
        pares.append(inputed)
    else:
        impares.append(inputed)

pares.sort()
impares.sort()
numlist.append(pares[:])
numlist.append(impares[:])

print('-='*20)
print(f'''Os valores pares digitados foram: {pares}
Os valores ímpares digitados foram: {impares}''')

