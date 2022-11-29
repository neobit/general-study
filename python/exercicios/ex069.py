# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
else:
    aluno['status'] = 'Reprovado'

print(f'''
Nome é igual a {aluno['nome']}.
Média é igual a {aluno['media']}.
Situação é igual a {aluno['status']}.
''')