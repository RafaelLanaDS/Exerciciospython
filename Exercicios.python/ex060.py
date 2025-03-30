''' Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

Aula anterior '''

# O que eu fiz !!!
#______________________________________________________________________________

n = int(input('Pense em um numero qualquer para saber a sua fatorial: '))

if n < 0:
    print('Não e possivel calcular a fatorial de um numero negativo')
else:
    fatorial = 1
    i = n
    while i > 1:
        fatorial  = fatorial * i
        i = i - 1
print('O fatorial de {} é {}' .format(n, fatorial))

#_______________________________________________________________________________

# O que vi no curso em video !!!


from math import factorial

n = int(input('Digite um numero para saber seu fatorial: '))
f = factorial(n)
print('A fatorial de {} e {}' .format(n, f))

#_________________________________________________________________________________

from time import sleep

n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
print('Calculando...')
sleep(2)
while c > 0:
    print('{}' .format(c) ,end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}' .format(f)) 

#__________________________________________________________________________________

n = int(input('Digite um numero para saber seu fatorial: '))
c = n
f = 1
for n in range(c):
    print('{}' .format(c) ,end='')
    print(' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}' .format(f))