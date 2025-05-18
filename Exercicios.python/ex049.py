'''Refaça o exercicio  009 mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.'''

num = int(input('Digite um numero para saber a sua tabuada: '))

for c in range (1, 11):
    print('{} X {:2} = {}' .format(num, c, num*c))
print('Tabuada finalizada !!')  