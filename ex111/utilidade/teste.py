'''
Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado
Trasfira todos as funçoes utilizadas nos desafios 107, 108 e 109
para o primeiro pacote e mantenha tudo funcionando
'''

from moedas import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p)