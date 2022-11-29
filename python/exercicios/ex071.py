# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime

actualYear = datetime.date.today().year
workerRegistry = dict()
workerRegistry['nome'] = str(input('Nome: '))
birthyear = int(input('Ano de nascimento: '))
workerRegistry['idade'] = actualYear - birthyear
ctps = int(input('Digite o número da sua Carteira de Trabalho [Digite apenas 0 caso não tenha]: '))
if ctps != 0:
    workerRegistry['ctps'] = ctps
    workerRegistry['contractyear'] = int(input('Digite o ano da sua contratação: '))
    workerRegistry['salary'] = float(input('Digite seu salário: R$ '))
    workerRegistry['aposentadoria'] = workerRegistry['idade'] + (30 - (actualYear - workerRegistry['contractyear']))
print('-='*30)

for x, y in workerRegistry.items():
    print(f'''O {x.capitalize()} tem o valor: {y}''')