# Faça um programa que tenha uma funcao chamada escreva(), que recebe um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = len(msg)
    print('-'*(tam+6))
    print('  ', msg)
    print('-'*(tam+6))

escreva(input('Digite a sua mensagem: '))