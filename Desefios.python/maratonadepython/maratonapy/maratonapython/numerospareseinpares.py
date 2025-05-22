'''
peça para o usuario digitar 7 numeros depois
separe os numeros em duas listas 
uma com pares e uma com os inpares
ao final mostre
todos os numeros digitados 
todos os pares digitados 
todos os impares digitados em ordem crescente
'''

lista = []
pares = []
impar = []

for c in range(0, 7):
    numeros = int(input('Digite um numero: '))   
    lista.append(numeros) # adiciona o numero a lista principal
    if numeros % 2 == 0: # verifica se o numero é par 
        pares.append(numeros) # lista par 
    else:
        impar.append(numeros) # lista impares 

print(f'{lista}') 
print(' numeros pares {}' .format(sorted(pares))) # sorted deixa em ordem os valores da lista 
print('mumeros impares {}' .format(sorted(impar)))  