''' Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
 O primeiro valor é MAIOR
 O segundo valor é MAIOR
 Não existe valor maior, os dois são IGUAIS
 '''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O primeiro valor {} é maior ' .format(n1))
elif n2 > n1:
    print('O segundo valor {} é maior' .format(n2))
elif n1 == n2:
    print('Os dois numeros são iguais:')