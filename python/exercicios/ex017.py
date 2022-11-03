# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensage mdizendo que ele foi multado. A multa vai custar R$7 por cada KM acima do limite.

import random

print('Lendo a velocidade atual do seu carro.')

carspd = random.randrange(0, 120)
multa = (carspd - 80)*7 

print('Dectamos que sua velocidade é {}km/h.'.format(carspd))

if carspd <= 80:
    print('O senhor estava dentro da máxima velocidade permitida na via, tenha um bom dia!')
else:
    print('Como o senhor ultrapassou a velocidade máxima permitida na via (80km/h) o senhor está sendo multado em R${}.'.format(multa))