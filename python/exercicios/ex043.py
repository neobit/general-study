# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesopessoas = []
for i in range (0, 5):
    inputed = int(input('Digite o peso da {}ª pessoa: '.format(i+1)))
    pesopessoas.append(inputed)

leve = 999
pesado = 0
for i in range (0, len(pesopessoas)):
    if pesopessoas[i] > pesado:
        pesado = pesopessoas[i]
    if pesopessoas[i] < leve:
        leve = pesopessoas[i]

print('A pessoa com {}kg é a mais leve e a com {}kg é a mais pesada.'.format(leve, pesado))