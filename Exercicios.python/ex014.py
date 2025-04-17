#escreva um programa que comverta uma temperatura digitada em C° e converta para  F°

c = float(input('Digite quantos graus C° esta agora: '))
f = c * 1.8 + 32
print('A temperatura de {}°C, corresponde há {}F°'.format(c, f))