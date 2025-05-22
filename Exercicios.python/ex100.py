'''
Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas
sortear() e  somapar()
a primereira função vai sortear 5 numeros e vai colocalos dentro da lista e a segunda fução vai mostrar todos os valores pares sorteados pela função anterior
'''
from random import randint

def sortear(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end='')
    print('  PRONTO')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista},  temos {soma}')

numeros = list()
sortear(numeros)
somapar(numeros)