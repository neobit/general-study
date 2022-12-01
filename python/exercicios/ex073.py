# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos o dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Ums lista com todas as pessoas com idade acima da média

cont  = ''
contDict = dict()
people = list()
womans = list()

while True:
    contDict['nome'] = input('Nome: ')
    contDict['sexo'] = ''
    while contDict['sexo'] != 'M' and contDict['sexo'] != 'F':
        contDict['sexo'] = input('Sexo [M/F]: ').upper()
        if contDict['sexo'] != 'M' and contDict['sexo'] != 'F':
            print('ERRO! Resposta inválida! Responda apenas com F ou M.')
    contDict['idade'] = int(input('Idade: '))
    people.append(contDict.copy())
    contDict.clear

    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continuar? [S/N]: ')).upper()
        if cont != 'S' and cont != 'N':
            print('ERRO! Resposta inválida! Responda apenas com S ou N.')
    if cont == 'N':
        break
    else:
        cont = ''
print('-='*30)
soma = 0
for i in range(0, len(people)):
    soma += people[i]['idade']
    if people[i]['sexo'] == 'F':
        womans.append(people[i]['nome'])
media = soma / len(people)
print(f'- O grupo tem {len(people)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {womans}')
print('- Lista de pessoas que estão acima da média:\n')

for i in range(0, len(people)):
    if people[i]['idade'] > media:
        print('nome = {0}; sexo = {1}; idade = {2}\n'.format(people[i]['nome'],people[i]['sexo'],people[i]['idade']))
print('<< ENCERRADO >>')