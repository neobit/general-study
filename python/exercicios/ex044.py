nomes = []
idade = []
sexo = []
age_media = 0
maisvelho = 0
mulheresnovas_qntd = 0
nomehomemmaisvelho = ''

print('==-=='*20)
print('\nIBGE Clone - Neobit | v0.01\n')
print('==-=='*20)

pessoa_qntd = int(input('\nInsira quantas pessoas você gostaria que fosse feito a média: '))

for i in range (0,pessoa_qntd):
    nomes.append(input('Digite o nome da {}ª pessoa: '.format(i+1)))
    idade.append(int(input('Digite a idade da {}ª pessoa: '.format(i+1))))
    sexo.append(input('Digite o sexo da {}ª pessoa (F: FEMININO | M: MASCULINO): '.format(i+1).upper()))

for i in range (0,pessoa_qntd):
    age_media += idade[i]
    if sexo[i] == 'M' and idade[i] > maisvelho:
        maisvelho = idade[i]
        nomehomemmaisvelho = nomes[i]
    if sexo[i] == 'F' and idade[i] < 20:
        mulheresnovas_qntd += 1

age_media = age_media / pessoa_qntd

print('A média de idade no grupo é: {:.0f}'.format(age_media))
if nomehomemmaisvelho != '':
    print('O nome do homem mais velho é {}'.format(nomehomemmaisvelho))
else: 
    print('Não há nenhum homem na lista.')
if mulheresnovas_qntd == 0:
    print('Não há nenhuma mulher na lista.')
elif mulheresnovas_qntd == 1:
    print('Há {} mulher com menos de 20 anos no grupo.'.format(mulheresnovas_qntd))
else:
    print('Há {} mulheres com menos de 20 anos no grupo.'.format(mulheresnovas_qntd))