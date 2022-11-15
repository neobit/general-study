# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numbers = (int(input(f'Digite o 1º número: ')), 
int(input(f'Digite o 2º número: ')), 
int(input(f'Digite o 3º número: ')), 
int(input(f'Digite o 4º número: ')))

print(f'Você digitou os valores: {numbers}')
if 3 in numbers:
    print(f'O valor 3 apareceu primeiro na {numbers.index(3)+1}ª posição.')
else:
    print(f'Não há nenhum 3 na lista digitada.')
    
print(f'''O valor 9 apareceu {numbers.count(9)} vezes.
Os valores pares digitados foram: ''', end='')
for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')
