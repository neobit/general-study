# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: a vista no dinheiro ou cheque = 10% de desconto, a vista no cartão de crédito = 5% de desconto, em até 2x no cartão de crédito = preço normal, 3x ou mais no cartão de crédito = 20% de juros no preço total

print('\033[0;31;40m')
print('==-=='*20)
print('\n\n\n Bem vindo ao sistema da loja da Konoha Ninja.\n\n\n')
print('==-=='*20)
print('\033[m')

price = float(input('Por favor, digite o valor do produto que você está comprando: R$'))

print('\n\nPor favor, selecione uma das opções de pagamento abaixo:\n1 - À vista (Dinheiro, Boleto, Pix)\n2 - À vista (Cartão)\n3 - Parcelado\n')
opt = int(input('Digite a opção desejada e aperte ENTER: '))

if opt == 1:
    print('\nA vista no boleto, pix ou cheque o senhor ganhou um desconto de 10%! O valor do produto ficou em R${:.2f}'.format(price*0.9))
elif opt == 2:
    print('\nA vista no cartão o senhor ganhou um desconto de 5%! O valor do produto ficou em R${:.2f}'.format(price*0.95))
elif opt == 3:
    opt2 = int(input('Por favor, digite em quantas vezes você quer parcelar (maximo 12 vezes): '))
    if opt2 <= 2:
        finalprice = price
    elif opt2 >= 3:
        finalprice = price*1.2
    print('\nParcelado em {} no cartão o valor do produto ficou em R${:.2f}. Em {} parcelas de R${:.2f}.'.format(opt2, finalprice, opt2, (finalprice)/opt2))