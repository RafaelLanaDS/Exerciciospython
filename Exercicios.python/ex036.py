''' Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
 da casa, o salario dp comprador e em quantos anos ele vai pagar
 Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salario ou então o enprestimo sera negado '''

valor_casa = float(input('Fale o valor da casa que deseja finaciar R$: '))
salario = float(input('Digite seu salario R$: '))
anos = int(input('Em quantos anos deseja pagar o finaciamento?: '))
mensal = valor_casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de {:.2f} ' .format(valor_casa, anos, mensal))
if mensal <= minimo:
    print('O emprestimo pode ser concedido')
else:
    print('Emprestimo negado')
    print('30% do seu lario foi {} POR conta disso o emprestimo de {} Mensal foi negado' .format(minimo, mensal))