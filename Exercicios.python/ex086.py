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


print('-=' * 30)
print("Matriz com as duas primeiras colunas repetidas:")
for l in range(3):
    linha_estendida = matriz[l] + matriz[l][0:2]
    for v in linha_estendida:
        print(f"{v:^5}", end='')
    print()

# Mostrando as diagonais principais
print('-=' * 30)
print("Diagonais principais (positivas):")
print(f"{matriz[0][0]} * {matriz[1][1]} * {matriz[2][2]} = {matriz[0][0] * matriz[1][1] * matriz[2][2]}")
print(f"{matriz[0][1]} * {matriz[1][2]} * {matriz[2][0]} = {matriz[0][1] * matriz[1][2] * matriz[2][0]}")
print(f"{matriz[0][2]} * {matriz[1][0]} * {matriz[2][1]} = {matriz[0][2] * matriz[1][0] * matriz[2][1]}")

# Mostrando as diagonais secundárias
print('-=' * 30)
print("Diagonais secundárias (negativas):")
print(f"{matriz[0][2]} * {matriz[1][1]} * {matriz[2][0]} = {matriz[0][2] * matriz[1][1] * matriz[2][0]}")
print(f"{matriz[0][1]} * {matriz[1][0]} * {matriz[2][2]} = {matriz[0][1] * matriz[1][0] * matriz[2][2]}")
print(f"{matriz[0][0]} * {matriz[1][2]} * {matriz[2][1]} = {matriz[0][0] * matriz[1][2] * matriz[2][1]}")

# Calculando o determinante
a = matriz[0][0] * matriz[1][1] * matriz[2][2]
b = matriz[0][1] * matriz[1][2] * matriz[2][0]
c = matriz[0][2] * matriz[1][0] * matriz[2][1]
d = matriz[0][2] * matriz[1][1] * matriz[2][0]
e = matriz[0][0] * matriz[1][2] * matriz[2][1]
f = matriz[0][1] * matriz[1][0] * matriz[2][2]

determinante = (a + b + c) - (d + e + f)

# Exibindo o determinante final
print('-=' * 30)
print(f"O determinante da matriz é: {determinante}")