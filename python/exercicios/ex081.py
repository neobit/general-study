# Crie um programa que tenha um função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálcullo do fatorial.

def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    Primeiro parametro: Número a ser fatorado
    Segundo parametro: Se vai exibir a conta completa no resultado ou não.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else: 
                print(' = ', end='')
        f *= c
    return f

inputed = int(input('Digite um número para realizar o fatorial: '))
print(fatorial(inputed, show=True))

help(fatorial)