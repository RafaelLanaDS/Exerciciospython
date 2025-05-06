'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = list ([[0,0,0],[0,0,0],[0,0,0]])
for l in range(0, 3):
    for c in range(0, 3): #Um laço dentro do anterior que percorre as colunas da matriz (de 0 até 2), formando uma combinação de cada posição [linha][coluna].
        matriz[l][c] = int(input("Digite um valor para cada {}, {}: " .format([l],[c]))) #Pede ao usuário um número para preencher a posição [l][c] da matriz.
print('-=' * 30)                                                                         #Aqui você usou uma f-string para mostrar os índices da célula ao usuário.
for l in range(0, 3): #Percorre novamente as linhas da matriz para exibir os valores já preenchidos.
    for c in range(0, 3): #Exibe os valores da matriz formatados com 5 espaços centralizados (:^5) em cada célula, sem pular de linha ao final de cada célula.
        print('[{:^5}]' .format(matriz[l][c]), end='')
    print()
        