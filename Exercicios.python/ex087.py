'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados:
    B) A soma dos valores da terceira coluna.
        C) O maior valor da segunda linha. 
'''
spar = 0
sterceira = 0
ssegunda = 0
matriz = list ([[0,0,0],[0,0,0],[0,0,0]])
for l in range(0, 3):
    for c in range(0, 3): #Um laço dentro do anterior que percorre as colunas da matriz (de 0 até 2), formando uma combinação de cada posição [linha][coluna].
        matriz[l][c] = int(input("Digite um valor para cada {}, {}: " .format([l],[c]))) #Pede ao usuário um número para preencher a posição [l][c] da matriz.
print('-=' * 30)                                                                         #Aqui você usou uma f-string para mostrar os índices da célula ao usuário.
for l in range(0, 3): #Percorre novamente as linhas da matriz para exibir os valores já preenchidos.
    for c in range(0, 3): #Exibe os valores da matriz formatados com 5 espaços centralizados (:^5) em cada célula, sem pular de linha ao final de cada célula.
        print('[{:^5}]' .format(matriz[l][c]), end='')
        if matriz[l][c] %2 == 0:
         spar = spar + matriz[l][c]
    print()
print('-=' * 30)
print('Ha soma dos valores pares digitados é {}' .format(spar))
print('-=' * 30)
for l in range(0, 3):
   sterceira = sterceira + matriz[l][2]
print('Há soma dos valores da terceira coluna foi {}' .format(sterceira))
print('-=' * 30)
for l in range(0, 3):
    if c == 0:
      ssegunda = matriz[1][c]
    elif matriz [1][c] > ssegunda:
      ssegunda = matriz[l][c]
print('O maior valor da segunda linha é {}' .format(ssegunda))