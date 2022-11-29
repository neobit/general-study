# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um bloetim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

opt = ''
aluno = list()
alunos = list()
media = 0

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    for i in range(0,2):
        aluno.append(float(input('Digite a primeira nota: ')))
    alunos.append(aluno[:])
    aluno.clear()
    opt = str(input('Deseja continuar? [S/N]: ')).upper()
    if opt == 'N':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i in range (0, len(alunos)):
    media = alunos[i][1] + alunos[i][2] / 2
    print(f'{i:<4}{alunos[i][0]:<10}{media:>8.1f}')
print('-'*30)

choose = 0
while True:
    choose = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if choose == 999:
        break
    print(f'Notas de {alunos[choose][0]} são: {alunos[choose][1]} e {alunos[choose][2]}')