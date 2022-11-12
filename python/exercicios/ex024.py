# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

import time

print('Olá, bem vindo ao sistema de financiamento imobiliário da NeobitBank.\nVamos precisar de algumas informações para fazer sua simulação.')
housevalue = int(input('Por favor, informe o valor da casa: R$'))
customersalary = int(input('Agora nos informe qual é o seu salário mensal: R$'))
paybackyear = int(input('Em quantos anos você planeja quitar o financiamento?: '))

monthlybill = housevalue / (paybackyear * 12)

print('Obrigado pelas informações.\n')
time.sleep(0.5)
print('Realizando simulação...')
time.sleep(3)

if monthlybill > customersalary * 0.3:
    print('Infelizmente devido a nossa analise das suas informações, teremos que negar o seu impréstimo devido as mensalidades (R${0:.2f}) representarem mais que 30 por cento do seu salário, que é de R${1}.'.format(monthlybill, customersalary))
else:
    print('Fizemos análise das suas informações e a oferta que podemos oferecer é de R${:.2f} mensais durante {} meses. '.format(monthlybill, paybackyear*12))