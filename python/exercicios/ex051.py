# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.

n = int(input('Quantos termos você quer exibir?: '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
counter = 3
while counter <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    counter += 1
print(' -> FIM')