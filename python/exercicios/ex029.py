# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos = mirim, até 14 anos = infantil, até 19 anos = junior, até 20 anos = senior, acima de 20 anos = master

idade = int(input('Insira a idade do nadador: '))

if idade <= 9:
    print('Esse nadador é da categoria MIRIM, visto que ele tem {:.0f} anos.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Esse nadador é da categoria INFANTIL, visto que ele tem {:.0f} anos.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Esse nadador é da categoria JUNIOR, visto que ele tem {:.0f} anos.'.format(idade))
elif idade > 19 and idade <= 20:
    print('Esse nadador é da categoria SÊNIOR, visto que ele tem {:.0f} anos.'.format(idade))
elif idade > 20:
    print('Esse nadador é da categoria MASTER, visto que ele tem {:.0f} anos.'.format(idade))