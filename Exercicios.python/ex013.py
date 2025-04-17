# Faça um algoritimo que leia o salario de um funcionario e mostre o seu salario com 15% de aumento.

salario = float(input('Digite seu salario R$: '))
novo_salario = salario + (salario * 15 / 100)
porcentagem = novo_salario - salario


print('Seu salario teve um reaguste de R${}, para um almento de R${}' .format(salario, novo_salario))
print('Voce teve um almento de 15%, ou seja R${:.2f}' .format(porcentagem))