# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

birthyear = int(input('Informe seu ano de nascimento: '))

militaryday = birthyear + 18
todayyear = (datetime.date.today()).year

if todayyear > militaryday:
    print('Você está atrasado para o serviço militar. Fazem {} anos que você deveria ter se alistado.'.format(todayyear-militaryday))
elif todayyear < militaryday:
    print('Ainda é cedo para se alistar, você irá se alistar daqui {} anos, no ano de {}.'.format(militaryday-todayyear, militaryday))
elif todayyear == militaryday:
    print('Você está em época de se alistar! Dirija-se a base militar mais próxima do seu local.')