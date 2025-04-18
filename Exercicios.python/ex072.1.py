lanche = 'hanburguer', 'suco', 'pizza', 'pudin'
# lanche[1] = 'sorvete' ERRO !! os elementos de uma tupla não podem ser alterados
for comida in lanche:
    print('Eu vou comer {}' .format(comida))
print('Estou satisfeito ')

print('----------------------------------------')
print(len(lanche))
print('----------------------------------------')
# OU


for cont in range(0, len(lanche)):
    print('Eu vou comer{}' .format(lanche[cont]))
print('Estou satisfeito ')

# tanto o for range e for lache vão fazer as mesma coisas
print('----------------------------------------')

'''SE PRECISAR VER A POSSIÇÃO DE CADA ITEN DA VARIAVEL UTILIZA ASSIM.'''

for cont in range(0, len(lanche)):
    print('Eu vou comer {} na posição {}' .format(lanche[cont], cont))
print('Estou satisfeito ')
