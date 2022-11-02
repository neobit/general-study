# Escreva um programa que leia um valor em metros e o exiba converido em centímetros e milímetros

n = int(input('Digite uma distância em metros: '))

print ('A medida de {0}m corresponde a:\n{1}km \n{2}hm \n{3}dam \n{4}dm \n{5}cm \n{6}mm'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))