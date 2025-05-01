'''
Crie um programa onde o usuario possa digitar vários valores numericos e cadastre em uma lista
caso o numero ja exista la dentro ele não sera adicionado 
no final exiba todos os valores únicos digitados em ordem crescente. 
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros: # verifica se o numero ja esta na lista
        numeros.append(n) # vai guardar os numeros digitados na lista  
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar') # não adicona o numero pois ja foi digitado 
    resp = ' '
    while resp not in 'SN': # repete ate o usuario digitar S ou N
        resp = str(input('Quer continuar S/N: ')).upper().strip()[0]
    if resp == 'N':
        break
numeros.sort()
print('Os valores digitados {}' .format(numeros))