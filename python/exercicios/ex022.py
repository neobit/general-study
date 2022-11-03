# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250, calcule um aumento de 10%. Para os inferiores ou iguais a R$1250, o aumento é de 15%.

print('Oi meu caro funcionário! Vamos te dar um aumento graças ao seu ótimo desempenho!')
salary = float(input('Informe seu salário atual: R$'))

if salary >= 1250:
    increase = salary * 1.1
else:
    increase = salary * 1.15

print('Seu salário será agora R${:.2f}. Seu salário aumento em {:.2f}!'.format(increase, increase-salary))