'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA, no final mostre os 10 primeiros termos dessa progressão'''

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range (10):
    decimo = termo + c * razao
    print('{}'.format(decimo), end=' > ')
print('ACABOU')

