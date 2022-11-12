# Faça um programa que o usuário insere um número e você mostre a tabuada desse número. Utilizando for range.

num = int(input('Insira o número que você gostaria de saber a tabuada: '))

print('===='*20)
for i in range(1,11):
    print('| {} vezes {} é {}'.format(num, i, num*i))
print('===='*20)