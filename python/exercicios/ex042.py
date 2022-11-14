# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 

from datetime import date
todayyear = (date.today()).year

anos = ''
maiores = []
menores = []
for i in range(0,7):
    anos = int(input('Insira o ano de nascimento da {}º pessoa: '.format(i+1)))
    if todayyear - anos < 18:
        menores.append(anos)
    else:
        maiores.append(anos)

print('Dos anos que você digitou, {} pessoas ainda não tem 18 anos e {} já são maiores de idade.'.format(len(menores),len(maiores)))