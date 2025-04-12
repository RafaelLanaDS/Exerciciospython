''' Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato
'''

soma = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Digite um produto: '))
    preço_produto = float(input('Fale o preço do produto: '))
    cont = cont + 1
    soma = soma + preço_produto

    if preço_produto >= 1000:
        totmil = totmil + 1
    
    if cont == 1:
        menor = preço_produto
        barato = produto
    else:
        if preço_produto < menor:
            menor = preço_produto
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if  resp == 'N':
        break 

print('Temos {} produtos que custaram mais de R$1000' .format(totmil))    
print('A soma dos produtos foi R${}' .format(soma))   
print('O produto mais barato foi {} que custa R${:.2f}' .format(barato ,menor))
