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

'''time = input("Digite o nome do time: ")
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
'''


# Contexto do programa:
# Sistema de Controle de Tarefas - "ToDo do João"
# João é um desenvolvedor iniciante e criou um sistema simples para organizar suas tarefas do dia a dia.
# Ele pode adicionar tarefas, visualizar todas as tarefas, marcar uma como concluída e remover tarefas.
# O sistema é executado no terminal e usa listas e estruturas condicionais.

# Lista onde as tarefas serão armazenadas
tarefas = []

# Loop principal do programa
while True:
    # Exibe o menu de opções
    print("\n=== ToDo do João ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")
    
    # Solicita a opção do usuário
    opcao = input("Escolha uma opção: ")

    # Opção 1: Adicionar tarefa
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append({"tarefa": tarefa, "concluida": False})  # Adiciona a tarefa como um dicionário
        print("Tarefa adicionada com sucesso!")

    # Opção 2: Ver tarefas
    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa adicionada.")
        else:
            print("\nLista de tarefas:")
            for i, t in enumerate(tarefas):
                status = "✅" if t["concluida"] else "❌"
                print(f"{i + 1}. {t['tarefa']} [{status}]")  # Mostra o status (concluída ou não)

    # Opção 3: Marcar como concluída
    elif opcao == "3":
        num = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["concluida"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número inválido.")

    # Opção 4: Remover tarefa
    elif opcao == "4":
        num = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= num < len(tarefas):
            removida = tarefas.pop(num)  # Remove a tarefa da lista
            print(f"Tarefa '{removida['tarefa']}' removida com sucesso.")
        else:
            print("Número inválido.")

    # Opção 5: Sair do programa
    elif opcao == "5":
        print("Encerrando o programa. Até mais!")
        break

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida. Tente novamente.")

# Autoavaliação:
# Acredito que mereço 10 pontos neste exercício, pois:
# ● Criei um contexto realista e útil para o programa (organizador de tarefas).
# ● Usei estruturas como listas, dicionários, loops e condicionais.
# ● Comentei as partes do código para facilitar o entendimento.
# ● Tratei possíveis erros de entrada e dei feedbacks claros ao usuário.










