# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distance = int(input('Informe a distância da viagem em Km: '))

if distance <= 200:
    pricetrip = distance * 0.5
else:
    pricetrip = distance * 0.45

print('O preço da sua viagem vai ser R${:.2f}.'.format(pricetrip))