''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

ex: Ana Maria de Sousa
Primeiro = Ana
ultimo = Sousa
'''

''' nome_completo = input("Digite seu nome completo: ").strip()
nomes = nome_completo.split()

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}") '''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer {}, seu nome começa com {''}, e termina com {''}' .format(n, nome[0], nome[-1]))
