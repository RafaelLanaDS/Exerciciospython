'''
Crie um programa que vai ler varios numeros e colocar em uma lista depois mostre.
A) quantos numeros foram digitasdos 
B) a lista de valores, ordenada de forma decrecente 
C) se o valor 5 foi digitado ou não na lista
'''

numeros = list()

while True:
    numeros.append (int(input('Digite um numero: ')))
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('Voce digitou {} elementos'.format (len(numeros)))
print('numeros em ordem decrecente {}' .format(sorted(numeros, reverse=True)))
if 5 in numeros:
    print('O numero cinco esta na lista')
else:
    print('O valor cinco não foi digtado')