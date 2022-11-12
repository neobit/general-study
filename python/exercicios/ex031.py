# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: Abaixo de IMC 18.5 = Abaixo do peso ideal, IMC entre 18.5 e 25 = Peso ideal, IMC de 25 até 30 = sobrepeso, IMC de 30 até 40 = Obesidade, IMC acima de 40 = Obesidade mórbida

altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite o seu peso atual em kg: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Como o resultado do seu IMC é de {:.1f}, seu status é de ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Como o resultado do seu IMC é de {:.1f}, seu status é de PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Como o resultado do seu IMC é de {:.1f}, seu status é de SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Como o resultado do seu IMC é de {:.1f}, seu status é de OBESIDADE.'.format(imc))
elif imc >= 40:
    print('Como o resultado do seu IMC é de {:.1f}, seu status é de OBESIDADE MÓRBIDA.'.format(imc))