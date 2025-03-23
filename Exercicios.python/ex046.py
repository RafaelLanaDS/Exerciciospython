'''Faça um programa que mostre na tela uma contagem regresiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1s entre eles '''
from time import sleep
print('contagem regresiva para os fogos !!!!!!')
for c in range(10, 0, -1): 
    print(c)
    sleep(1)
else:
    print('FELIZ ANO NOVO !!!!')