'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionario
se por acaso a CTPS for difrente de ZERO, o dicionario recebera tambem o ano de contratação e o salario,
calcule o acrescimo alem da idade com quantos anos a pessoa vai se aposentar
'''

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario']  = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35 ) -  datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'-  {k} tem o valor {v}')