# Receba um número e apresente na tela o dobro, o triplo e a raiz quadrada desse número.
n = int(input('Digite um número: '))
print('O dobro de {0} vale {1}. \n O triplo de {0} é {2} \n A raiz quadrada de {0} é {3}.'.format(n, n*2, n*3, pow(n, (1/2))))