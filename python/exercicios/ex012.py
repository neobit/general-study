# Receba o nome de 4 alunos, exiba na tela apenas um aluno sorteado.
from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)
print('O aluno escolhido foi o {}.'.format(escolhido))