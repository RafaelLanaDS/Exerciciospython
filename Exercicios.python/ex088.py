'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em um lista composta 
'''

from random import randint
from time import sleep
lista = list ()
jogos = list ()
print('-='*30)
print('                     JOGUE NA MEGA SENA             ')
print('-='*30)
quant = int(input('Quantos jogos você que eu sortei? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break   
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}:{l}')
    sleep(2)
print('-='*5, 'BOA SORTE', '-='*5)