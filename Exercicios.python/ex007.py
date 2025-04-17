# Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua media

n1 = float(input('digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2
print(' a media de {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, m))
