# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

interv_final = int(input('Digite o intervalo máximo da ordem númerica: '))
opt = int(input('''Selecione se você quer que seja exibido apenas os impares ou pares:
DIGITE 1 PARA PAR
DIGITE 2 PARA IMPAR
DIGITE A SUA OPÇÃO:'''))

if opt == 1:
    opta = 0
elif opt == 2:
    opta = 1
else:
    print('Opção inválida! Finalizando a execução.')
    exit()

for i in range(1,interv_final+1):
    if (i % 2) == opta:
        print(i, ' ', end='')