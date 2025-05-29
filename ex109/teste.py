'''
modifique as funçoes que form criadas no desafio 107 para que elas aceitem um parâmetro e mais, 
informando se o valor retornado por elas vai ser ou não formatada pela função moeda(), Desenvolvida no desafio 108
'''


import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando o preço em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo o preço em 13%, temos {moeda.diminuir(p, 13, True)}')