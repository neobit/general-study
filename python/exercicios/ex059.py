# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numbers = []
while True:
    inputed = int(input('Digite um valor: '))
    if inputed not in numbers:
        numbers.append(inputed)
        print('Valor adicionado com sucesso...')
        opt = input('Quer continuar? [S/N]: ').upper()
        if opt == 'N':
            break
    else:
        print('Valor repetido, tente novamente. ')

numbers.sort()
print('-='*30)
print(f'Você digitou os valores: {numbers}')