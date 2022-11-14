# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

auth = True
inputed = ''
while auth == True:
    inputed = input('Digite o seu sexo [Masculino/Feminino]: ').upper()
    if inputed == 'MASCULINO' or inputed == 'FEMININO':
        auth = False
        print('Obrigado pela informação.')
    else:
        print('Opção inválida. Digite novamente!')