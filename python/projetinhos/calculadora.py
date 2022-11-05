from time import sleep

choice = -1
result = 0
n1 = 0
n2 = 0

def first_screen():
    print('\033[0;31;40m')
    print('==-=='*20)
    print('Oi, eu sou uma calculadora.')
    print('==-=='*20)
    print('\033[m')
    print('Selecione uma operação:\n1.Adição\n2.Subtração\n3.Divisão\n4.Multiplicação\n5.Potênciação')
    choice = input('Digite a opção desejada e aperte ENTER: ')
    screen_selector(choice)

def screen_selector(inputed):
    if inputed.isdigit():
        choice = int(inputed)
    #    print('Convertido com sucesso')
        if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
            operations(choice)            
        else:
            print('\033[0;31;40m')
            print('\n Opção inválida! Tente novamente.\n')
            print('\033[m')
            sleep(2)
            first_screen()
            return
    else:
        print('\033[0;31;40m')
        print('\n Opção inválida! Tente novamente.\n')
        print('\033[m')
        sleep(2)
        first_screen()
        return

def operations(opt):
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o primeiro número: '))
    match opt:
        case 1:
            result = n1 + n2
            print('O resultado da adição de {} + {} é: {}'.format(n1, n2, result))
        case 2:
            result = n1 - n2
            print('O resultado da subtração de {} - {} é: {}'.format(n1, n2, result))
        case 3:
            result = n1 / n2
            print('O resultado da divisão de {} por {} é: {}'.format(n1, n2, result))
        case 4:
            result = n1 * n2
            print('O resultado da multiplicação de {} x {} é: {}'.format(n1, n2, result))
        case 5:
            result = n1 ** n2
            print('O número {} elevado a {} é: {}'.format(n1, n2, result))
    sleep(2)
    first_screen()

first_screen()