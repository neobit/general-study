# Refaça o exercicio 39, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

firsterm = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
maxterm = (firsterm + (10 - 1)*razao)+1

counter = 0
while counter <= maxterm:
    print(counter, end=' -> ')
    counter += razao
print('Acabou')