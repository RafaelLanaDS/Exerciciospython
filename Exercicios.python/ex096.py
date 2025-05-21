'''
Faça um programa que tenha uma função chamada area()
que recebe as dimençoes de um terreno rentangular [LARGURA X COMPRIMENTO]
e mostre a largura do terro.
'''
def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} X {comp} é de {a}M²')



print('-' *20)
print('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)