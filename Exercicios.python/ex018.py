# Faça um programa que leia um angulo qualquer e mostre na tela o valor da seno cosseno e tangente desse angulo


import math

angulo = float(input('Digite um angulo qualquer: '))

# Conversão para radianos
radianos = math.radians(angulo)

# Cálculo das funções trigonométricas
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Exibição dos resultados
print("Seno: {:.2f} " .format(seno))
print("Cosseno: {:.2f} " .format(cosseno))
print("Tangente: {:.2f}" .format(tangente))
