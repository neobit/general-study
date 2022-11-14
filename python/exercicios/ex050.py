# Refaça o exercicio 49, fazendo com que seja possivel continuar mostrando termos.

Programa = True
firsterm = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
maxterm = (firsterm + (10 - 1)*razao)+1

counter = 0

while Programa == True:
    while counter <= maxterm:
        print(counter, end=' -> ')
        counter += razao
    print('Acabou')
    print('Counter: {}'.format(counter))
    opt = int(input('Quer que mostre mas quantos termos dessa progressão?: '))
    if opt == 0:
        print('Finalizando programa.')
        Programa = False
    elif opt <0:
        print('Opção inválida. Finalizando programa.')
        Programa = False
    else:
        maxterm = maxterm + opt*2