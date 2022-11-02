# Peça os catetos do triangulo retângulo e informe o valor da hipotenusa.

from math import sqrt

catOp = float(input('Informe o valor do cateto oposto do triangulo: '))
catAd = float(input('Informe o valor do cateto adjacente do triangulo: '))

hip = sqrt(catOp**2 + catAd**2)

print('O valor da hipotenusa é: {:.2f}'.format(hip))