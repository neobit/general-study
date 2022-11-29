# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint as random

opt = int(input('Digite quantos jogos da mega sena você quer gerar: '))
jogos = list()
jogo = list()

for i in range(0, opt):
    for i in range(0, 6):
        jogo.append(random(1, 61))
    jogos.append(jogo[:])
    jogo.clear()

print('-='*25)

for i in range (0, len(jogos)):
    print(f'O {i+1}º sorteio foi: {jogos[i]}')