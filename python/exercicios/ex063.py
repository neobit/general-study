# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Digite a expressão: '))
listinha = []
for simb in expression:
    if simb == '(':
        listinha.append('(')
    elif simb == ')':
        if len(listinha) > 0:
            listinha.pop()
        else:
            listinha.append(')')
            break
if len(listinha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta.')