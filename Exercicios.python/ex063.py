'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8

Aula Anterior
'''
print('Digite um numero para saber os elementos de uma sequencia de Fibonacci.')
n1 = int(input('Quantos termos voce quer mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}' .format(t1, t2), end='')
cont = 3

while cont <= n1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' -> {}' .format(t3), end='')
    
    cont = cont + 1 
print(' -> FIM')