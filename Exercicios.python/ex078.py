'''
Faça um programa que leia 5 valores numericos e guarde-os em uma lista 
No final mostre qual foi o maior numero digirado e as suas respectivas posições na lista.
'''

 # O programa que le 5 numeros e mostrar o maior o menor e suas possições 
numeros = list () # lista para gaurdar os numeros digitados 
maior = 0 # Vai guardar o maior numero
menor = 0 # vai guardar o menor numero 
for c in range(0, 5): #  
    numeros.append(int(input('Digite um numero para a posição {}: ' .format(c)))) # le um numero e adiciona na lista
    if c == 0: # se for o primeiro numero ele sera o maior e o menor por enquanto
       maior = menor = numeros[c] 
    else:
        if numeros[c] > maior: # atualiza o maior numero se o atual for o maior 
             maior = numeros[c]
        if numeros[c] < menor: # atualiza o menor numero se o atual for o menor
            menor = numeros[c]
        
print('Voce digitou os valores {}' .format(numeros)) #mostra todos os numeros digitados 

print('O maior numero digitado foi {} nas possições'.format(maior), end='' ) # mostra o maior numero e suas possiçoes 
for i, v in enumerate(numeros): # pega a posição (i) e o valor (v)
    if v == maior:
        print(' {}....'.format(i), end='') # mostra a posição do maior 


print() # quebra a linha 
print('O menor numero digitado foi {} nas possições '.format(menor), end='' )
for i, v in enumerate(numeros):
    if v == menor:
        print(' {}....' .format(i), end='') # mostra a posição do menor 
print()# quebra a linha 