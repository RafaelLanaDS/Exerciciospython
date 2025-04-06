'''
Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario
o programa sera interrompido quando o numero solicitado for negativo.
'''


while True:
    n = int(input('Digite um numero para saber sua tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        print('{} X {} = {}' .format(c, n, c*n))
print('Fim volte sempre!!')
    