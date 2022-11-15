# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numbers = list()
for i in range(0, 5):
    numbers.append(int(input(f'Digite o {i+1}º valor: ')))
print('-='*20)
print(f'Você digitou os valores: {numbers}')
print(f'O maior valor digitado foi {max(numbers)} nas posições: ', end='')
for i in range(0, len(numbers)):
    if numbers[i] == max(numbers):
        print(i+1, end=' ')
print(f'\nO menor valor digitado foi {min(numbers)} nas posições: ', end='')
for i in range(0, len(numbers)):
    if numbers[i] == min(numbers):
        print(i+1, end=' ')