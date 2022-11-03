from time import sleep
from sys import exit

accounts = ['cafemolhado', 'bananacosmica']
passwords = ['sabequemsabe', 'nadaaver']
optionchoosed = ''

def first_screen():
    print('\033[0;31;40m')
    print('==-=='*20)
    print('\n Bem vindo ao sistema escolar da Konoha Ninja School.\n')
    print('==-=='*20)
    print('\033[m')
    print('Por favor, selecione uma das opções abaixo:\n1 - Fazer Login\n2 - Criar nova Conta\n')
    inputed = input('Digite a opção desejada e aperte ENTER: ')
    screen_selector(inputed)

def screen_selector(inputed):
    if inputed.isdigit():
        optionchoosed = int(inputed)
    #    print('Convertido com sucesso')
        if optionchoosed == 1 or optionchoosed == 2:
            match optionchoosed:
                case 1:
                    login_system()
                case 2:
                    register_system()
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

def user_logged():
    exit()

def outputs(loginstatus):
    match loginstatus:
        case 'loginsuccess':
            print('Logado com sucesso!')
            user_logged()
        case 'wrongpassword':
            print('\033[0;31;40m')
            print('Senha incorreta. Redirecionando para a tela principal...')
            print('\033[m')
            sleep(2)
            first_screen()
        case 'logindonotexist':
            print('\033[0;31;40m')
            print('O login digitado não existe no banco de dados. Redirecionando para a tela principal...')
            print('\033[m')
            sleep(2)
            first_screen()
        case 'registersuccess':
            print('Conta criada com sucesso! Agora você pode realizar login na tela principal!')
            sleep(2)
            first_screen()
        case 'error404':
            print('Erro inexperado! Voltando a tela principal.')
            sleep(2)
            first_screen()

def login_system():
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
    i = 0
    while i <= len(accounts):
        if login == accounts[i-1]:
            if senha == passwords[i-1]:
                outputs('loginsuccess')
            else:
                outputs('wrongpassword')
        elif i < len(accounts):
            i = i + 1
        elif i == len(accounts) and login != accounts[i-1]:
            outputs('logindonotexist')
        else:
            outputs('error404')
        
def register_system():
    accounts.append(str(input('Digite seu novo login: ')))
    newsenha = str(input('Digite sua nova senha: '))
    senhaconfirmation = str(input('Confirme sua nova senha: '))
    if newsenha == senhaconfirmation:
        passwords.append(newsenha)
        newsenha = ''
        senhaconfirmation = ''
        outputs('registersuccess')

first_screen()


