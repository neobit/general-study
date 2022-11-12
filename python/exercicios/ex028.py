# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5 = reprovado, média entre 5 e 6.9 = recuperação, média 7 ou superior = aprovado.
import time

nota1 = int(input('Insira a nota da sua primeira prova: '))
nota2 = int(input('Insira a nota da sua segunda prova: '))

print('Calculando a sua média\nPor favor, aguarde...')
time.sleep(3)

media = (nota1 + nota2) / 2

if media < 5:
    print('Você ficou com média {:.1f}. Você foi reprovado!'.format(media))
elif 5 <= media and media < 7:
    print('Você ficou com média {:.1f}. Você está de recuperação!'.format(media))
elif media >= 7:
    print('Você ficou com média {:.1f}. Você foi aprovado! Parabéns!!!'.format(media))