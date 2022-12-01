# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, comp):
    area = lar * comp
    print(f'A área de um terreno {lar:.2f}x{comp:.2f} é de {area:.2f}m².')

def title(msg):
    print(msg)
    print('-'*20)

title('Controle de Terrenos')
area(float(input('Digite a largura do terreno (m): ')), float(input('Digite o comprimento do terreno (m): ')))
