# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# Aprimore o desafio, mostrando no final:
# A) A soma de todos os valores pare digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
soma1 = soma2 = biggerNum = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor do eixo {l}x{c} da matriz: '))
        if matriz[l][c] % 2 == 0:
            soma1 = soma1 + matriz[l][c]
        if c == 2:
            soma2 = soma2 + matriz[l][c]
        if l == 1 and matriz[l][c] > biggerNum:
            biggerNum = matriz[l][c]

print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-='*20)
print(f'''A soma dos valores pares é {soma1}.
A soma dos valores da terceira coluna é {soma2}.
O maior valor da segunda linha é {biggerNum}.''')