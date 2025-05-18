'''
Crie um programa que leia nome, sexo e idade de varias pessoas guardando em uma os dados de cada pessoa em um dicionario
e todos os dicionario em uma lista
No final, mostre.
A) Quantas pessoas foram cadastradas
B) A media de idade 
C) uma lista com as mulheres 
D) uma lista de pessoas com idade acima da media
'''

pessoas = dict()
lista = list()
n_pessoas = 0
media_idade = 0
lista_F = 0

while True:
    pessoas['Nome'] = str(input('Nome: '))
    n_pessoas = n_pessoas + 1
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoas['idade'] = int(input('Idade: '))

    lista.append(pessoas.copy())
    print()

    sair = str(input('Escreva [SAIR] para encerrar o programa ou aperte [ENTER] para continuar: ')).upper()
    if 'SAIR' in sair:
        break

print('-=' * 30)
print('Lista de pessoas cadastradas:')
for p in lista:                      #"Para cada pessoa (p) dentro da lista, execute o bloco de código abaixo."
    print(f"Nome: {p['Nome']}\nSexo: {p['sexo']}\nIdade: {p['idade']}\n" + '-' * 20)
print('-=' * 30)

print(f'foram Cadastradas {n_pessoas} pessoas')
print('-=' * 30)

print('Lista de mulheres cadastradas:')
for p in lista:
    if p['sexo'] == 'F':
        print(f"Nome: {p['Nome']}")
print('-=' * 30)

soma_idades = 0
for p in lista:
    soma_idades += p['idade']

media_idade = soma_idades / len(lista)
print(' A média de idade é {:.2f}'.format(media_idade))

print('-=' * 30)
print(' Pessoas com idade acima da média:')
for p in lista:
    if p['idade'] > media_idade:  # verifica se a idade é maior que a média
        print(f"Nome: {p['Nome']}, Idade: {p['idade']}, Sexo: {p['sexo']}")