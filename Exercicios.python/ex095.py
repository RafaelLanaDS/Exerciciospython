'''
Aprimore o desafio 93 para que ele funcione com varios jogadores incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador
'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('Erro, responda SIM ou NÃO')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}' , end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    Busca = int(input('Mostrar dados de qual jogador, (999) para parar'))
    if Busca == 999:
        break
    if Busca >= len(time):
        print(f'ERRO não existe jogador com codigo {Busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR{time[Busca]["nome"]}: ')
        for i, g in enumerate(time[Busca]['gols']):
            print(f'     no jogo {i+1} fez {g} gols')
    print('-=' * 40)
print()
    