'''
peça para o usuario digitar 7 numeros depois
separe os numeros em duas listas 
uma com pares e uma com os inpares
ao final mostre
todos os numeros digitados 
todos os pares digitados 
todos os impares digitados em ordem crescente
'''

lista = list()

for c in range(0, 4):
    lista.append (int(input('Digite um numero: ')))
    
print(' os numeros digitados foram {}' .format(lista))
for v, i in enumerate(lista):
    if v % 2 == 0:
        print('Esses foram os numeros pares digitados {}' .format(i))
    else:
        print('Os numeros inpares foram {}' .format(i))