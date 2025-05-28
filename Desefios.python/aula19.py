pessoas = dict({'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22})

del pessoas['Sexo'] # apaga o valor sexo
pessoas['Nome'] = 'Leandro' # muda o valor do nome
pessoas['peso'] =  98.5 #adiciona um novo valor ao dicionario

print(pessoas['Nome'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
 
print('-=' * 6)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 6)
# Adicionando um dicionario dentro de uma lista.

brasil = list() #criando uma lista
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'} 
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'} 
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])

print('-=' * 6)

brasil = list()
estado = dict()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Usar .copy() é MUITO IMPORTANTE! Sem isso, todos os itens da lista apontariam para o mesmo dicionário, e qualquer mudança afetaria todos ao mesmo tempo.
for e in brasil:                          # Dentro de cada dicionário, você está pegando os valores (sem as chaves).
    for v in e.values():                  # para {'UF': 'São Paulo', 'SIGLA': 'SP'}, e.values() vai dar: 'São Paulo' e 'SP'
        print(v, end=' ')                 # Para {'UF': 'Rio de Janeiro', 'SIGLA': 'RJ'}, vai dar: 'Rio de Janeiro' e 'RJ'
    print()
