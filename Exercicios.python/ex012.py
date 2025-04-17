#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preço = float(input('Digite o preço do produto R$: '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com 5% de desconto custara R${:.2f}' .format(preço, novo))