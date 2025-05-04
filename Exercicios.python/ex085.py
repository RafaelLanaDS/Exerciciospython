'''
Crie um programa onde o usuario digite sete valores numericos e cadastre- os em uma lista unica que mantenha separados os valores pares e inpares 
no final mostre os valores pares e impares em ordem crescente.
'''
num = list ([[], []])
valor = 0
for c in range(1, 8):
    valor = int(input('Digite o {}º valor: ' .format(c)))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('todos os valores {}' .format(num))
num[0].sort()
print('Esses são os valores pares {}' .format(num[0]))
num[1].sort()
print('E esse são os valores impares {}' .format(num[1]))