# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa

from math import sqrt

# Leitura dos catetos
cateto_oposto = float(input("Digite um numero: "))
cateto_adjacente = float(input('Digite outro numero '))

# Cálculo da hipotenusa
hipotenusa = (cateto_oposto**2) + (cateto_adjacente**2)

print("O comprimento da Hipotenusa é {:.2f}" .format(sqrt(hipotenusa)))