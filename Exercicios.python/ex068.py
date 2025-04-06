'''Faça um programa que jogue par ou impar com o computador. O jogo so sera intenrronpido quando
o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''

from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' 
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [P/I]: ')).strip().upper()[0]
    print('Jogador jogou {} e computador {} , a soma entre os dois foi {}' .format(jogador, computador, total))
    print('Deu par' if total %2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            v = v + 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':   
        if total % 2 == 1:
            print('Voce ganhou')
            v = v + 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print('Game over voce ganho {} vezes' .format(v))
            