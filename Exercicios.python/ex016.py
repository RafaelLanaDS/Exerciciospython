# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: digite um numero:6.127, o numero {} tem a parte inteira 6

import math

# Solicita ao usuário um número real
num = float(input("Digite um número: "))

# Obtém a parte inteira usando int()
parte_inteira = int(num)

# Alternativamente, podemos usar math.trunc()
# parte_inteira = math.trunc(num)

# Exibe o resultado
print("O número {} tem a parte inteira {}." .format(num, parte_inteira))