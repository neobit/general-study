# Faça um programa que leia um angulo qualquer e mostre na ela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, tan, sin, radians

ang = float(input('Informe um angulo qualquer: '))

seno = sin(radians(ang))
print('O angulo de {} tem como SENO o valor de: {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem como COSSENO o valor de: {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem como TANGENTE o valor de: {:.2f}'.format(ang, tangente))