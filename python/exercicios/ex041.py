# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

# frase = 'Oi eue ioi iO'
frase = 'Oi eu nao sou um palindromo'
lenfrase = len(frase)

frase_contraria = ''
for i in range(lenfrase, 0, -1):
    frase_contraria = frase_contraria + frase[i:i]
    print(i)

print(frase_contraria)