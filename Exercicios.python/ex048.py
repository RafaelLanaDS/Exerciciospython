'''Faça um program que calcule todos os numeros impares  que são multiplos de tres e que se encontra no intervalo de 1 ate 500'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
    
print('A soma de todos os {} valores solicitados é {}' .format(cont, soma))
