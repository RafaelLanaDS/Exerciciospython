''' Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
para salarios superiores a 1.250 calcule um aumento de 10%
para inferiores ou iguais o aumento é de 15% '''

salario = float(input('Digite seu salario em R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R$ {} passa aganhar R${} agora.' .format(salario, novo))