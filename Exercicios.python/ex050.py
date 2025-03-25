'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daquelas que forem pares, se o valor digitado for impar desconsidereo'''
soma = 0
for c in range(6):
    num = int(input('Digite um numero: '))
    if num %2 == 0:
        soma = soma + num
print('A soma dos numeros pares da lista {}' .format(soma))
