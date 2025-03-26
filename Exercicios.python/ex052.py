'''Faça um programa que leia um numero interio e diga se ela é ou não um numero primo'''

n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31', end='')
    print('{}' .format(c), end='')
print('\n\033[m O numero {} foi divisivel {} vezes' .format(n1, tot))   
if tot == 2:
    print('E POR ISSO ELE É PRIMO')
else:
    print('E POR ISSO ELE NÃO É PRIMO')