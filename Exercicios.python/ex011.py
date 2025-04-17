#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área ea quantidade de tinta necessaria para pinta-la
#sabendo que a cada litro de tinta pinta uma area de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pinta essa parede, voce precisara de {}l de tinta' .format(tinta))