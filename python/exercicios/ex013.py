# Receba 4 nomes de alunos e sorteie a ordem do qual eles irão apresentar o trabalho.

import random

nome1 = input('Escreva o primeiro nome: ')
nome2 = input('Escreva o segundo nome: ')
nome3 = input('Escreva o terceiro nome: ')
nome4 = input('Escreva o quarto nome: ')
nomes = [nome1, nome2, nome3, nome4]

random.shuffle(nomes) # O comando só realiza o shuffle na variavel, basta apenas cita-a depois.

print('A ordem da apresentação será: \n{}'.format(nomes))