''' s = 0 
for c in range (0, 4):
    n =  int(input('Digite um valor: '))
    s = s + n
print('O somatorio de todos os valores foi {}' .format(s)) '''
  
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIm')'''

time = input("Digite o nome do time: ")
rodada = 1
pontos = 0
vitorias = 0
empates = 0
derrotas = 0

while True:
    print(f"Rodada {rodada}")
    resultado = input("Digite o resultado (V para vitória, E para empate, D para derrota ou 0 para sair): ").strip().upper()
    
    if resultado == '0':
        break
    elif resultado == 'V':
        pontos += 3
        vitorias += 1
    elif resultado == 'E':
        pontos += 1
        empates += 1
    elif resultado == 'D':
        derrotas += 1
    else:
        print("Opção inválida. Digite V, E, D ou 0.")
        continue
    
    print(f"Total de pontos: {pontos}\n")
    rodada += 1

print(f"\nResumo do campeonato para {time}:")
print(f"Vitórias: {vitorias}, Empates: {empates}, Derrotas: {derrotas}")
print(f"Pontuação final: {pontos}")

if pontos > 20:
    classificacao = "Libertadores"
elif pontos > 15:
    classificacao = "Sulamericana"
elif pontos < 5:
    classificacao = "Rebaixamento"
else:
    classificacao = "Meio de tabela"

print(f"Classificação: {classificacao}")

