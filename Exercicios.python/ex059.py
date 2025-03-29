''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
[
Seu programa deverá realizar a operação solicitada em cada caso. '''

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('''
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
escolhido = int(input('Qual operçao desseja escolher ?'))
while escolhido in (1,6):
    if escolhido == 1:
        print('A soma entre numero {} e numero {} foi {}' .format(n1, n2, n1 + n2))
    elif escolhido == 2:
        print('A multiplo]icação entre {} e {} é {}' .format(n1, n2, n1 * n2))
    elif escolhido == 3:
        print('A m')
print('Acabou')