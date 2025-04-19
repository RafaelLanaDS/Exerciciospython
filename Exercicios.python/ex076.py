'''
Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços organizando os dados em forma tabular.
'''
print('-' * 40)
print('{:^40}' .format("LISTAGEM DE PREÇOS"))
print('-' * 40)

produtos = ('lapis', 1.75,
            'borracha', 2.00,
            'caderno', 15.90,
            'estojo', 25.00,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'canetas', 22.30,
            'livros', 34.90)

for c in range(0, len(produtos)):
    if c % 2  == 0:
        print('{:.<30}'.format(produtos[c]), end=' ')
    else:
        print('R${:>7.2f}' .format(produtos[c]))