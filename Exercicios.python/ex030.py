''' Crie um programa que leia um numero e mostre na tela se ele é par ou impar
Como usar o módulo
Divida o número por 2
Se o resto for zero, o número é par
Se o resto for diferente de zero, o número é ímpar
'''

'''n = int(input('Digite um numero qualquer: '))
if n %2 == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')'''

n = int(input('Digite um numero para saber seu termo: '))
t1 = 0
t2 = 1
print('{} -> {} ' .format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}' .format(t3) , end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('-> FIM')