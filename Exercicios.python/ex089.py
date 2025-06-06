'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

ficha = list() #lista principal
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media]) # aqui guarda todas as informaçoes separando (NOME (NOTA1, NOTA2) (MEDIA))
  resp = str(input('Quer continuar? [S/N]')) # verifica se quer continuar [S/N]
  if resp in 'Nn':
    break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}') # exibe o cabeçalho da tabela
print('-' * 26)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # mostra o boletin resumido com nome e media de cada aluno
while True:
  print('-' * 35)
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc <= len(ficha) - 1: #verifica se o indice digitado é valido
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')