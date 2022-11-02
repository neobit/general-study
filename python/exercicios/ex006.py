# Receber duas notas de um aluno e dar a média das notas.

nt1 = float(input('Insira a primeira nota: '))
nt2 = float(input('Insira a segunda nota: '))

input('A média entre {0:.1f} e {1:.1f} é: {2:.1f}'.format(nt1, nt2, (nt1+nt2)/2))

# o ":.1f" significa que o valor terá 1 casa decimal e arredondará para cima.