# Recebe o nome completo da pessoa, exibe o nome todo com letra maiuscula e todo com letra minuscula. Conta quantas letras tem e mostra apenas o primeiro nome e quantas letras o primeiro nome tem.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando o seu nome...')
print('Seu nome em maiusculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome.replace(" ", ""))))

nomesplited = nome.split()

print('Seu primeiro nome é {0} e ele tem {1} letras.'.format(nomesplited[0], len(nomesplited[0])))
