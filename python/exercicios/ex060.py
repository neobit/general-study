# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostra a lista ordenada na tela.

numbers = list()
for i in range (0, 5):
    inputed = int(input('Insira um número: '))
    if i == 0 or inputed > numbers[-1]:
        numbers.append(inputed)
        print('Adicionado ao final da lista.')
    else:
        x = 0
        while x < len(numbers):
            if inputed <= numbers[x]:
                numbers.insert(x, inputed)
                print(f'Adicionado na posição {x} da lista.')
                break
            x += 1

print(f'Os números foram: {numbers}')