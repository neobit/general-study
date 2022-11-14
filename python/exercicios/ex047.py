# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

Programa = True
opt = 0



while Programa == True:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o primeiro número: '))

    print('''Digite a opção desejada:
    [1] Somar.
    [2] Multiplicar.
    [3] Qual número é maior.
    [4] Digitar os números novamente.
    [5] Fechar o programa.
    ''')
    opt = int(input('Digite a sua opção: '))
    if opt == 1:
        result = num1 + num2
        print('A soma entre {} e {} é igual a: {}'.format(num1, num2, result))
        Programa = False
    elif opt == 2:
        result = num1 * num2
        print('{} multiplicado por {} é igual a: {}'.format(num1, num2, result))
        Programa = False
    elif opt == 3:
        if num1 > num2:
            print('O maior número é o {}. Pois o número {} é menor'.format(num1, num2))
            Programa = False
        else:  
            print('O maior número é o {}. Pois o número {} é menor'.format(num2, num1))
            Programa = False
    elif opt == 5:
        Programa = False