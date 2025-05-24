'''
Faça um progrma que tenha uma função chamda ficha() que receba dos parametros opicionais
O nome de um jogador e quantos gols ele marcou
o programa devera ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente
'''


def ficha(jog='Desconhecido', gol=0):
    print(f'O jogado {jog} fez {gol} gols no campeonato ')



#PROGRAMA PRINCIPAL
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols feitos: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
    
