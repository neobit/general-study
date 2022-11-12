# Faça um programa que calcule a soma entre todos os número ímpares que são múltiplos de três que se encontram o intervalo de 1 até 500.

soma = 0
for i in range(1,501):
    if (i % 3) == 0:
        soma += i

print('A soma de todos os número multiplos de 3 presentes entre 1 e 500 é: {}'.format(soma))