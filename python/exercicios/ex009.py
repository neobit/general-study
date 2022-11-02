# Faça um conversor de moedas para USD.

money = float(input('Informe quando dinheiro você tem na carteira. R$'))

print('Com R${0:.2f} você pode comprar USD${1:.2f}'.format(money, money/5.14))