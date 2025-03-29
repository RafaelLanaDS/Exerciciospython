''' Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

# O QUE EU FIZ !!!

from random import randint

numero = randint(0,10) #numero que o computador ira pensar de 1 a 10
palpite = int(input('Tente acertar um numero de 0 a 10:'))
tentativas = 0
while palpite != numero:
    palpite = int(input('Seu palpite esta errado tente novamente: '))
    tentativas = tentativas + 1
    if palpite == numero:
        print('Seu palpite esta correto {}' .format(palpite))
print('Foram necessarios {} palpites ate voce acertar' .format(tentativas))

#  O QUE VI NA AULA DO CUSTAVO GUANABARA

computador = randint(0, 10)
print('Eu sou computador... Acabei de pensar em um numero entre 0 a 10')
print('Sera que voce consegue adivinhar qual foi ?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite: "))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente novamente')
print('Acabou. Foram necessarias {} tentativas ate acertar o numero escolhido ' .format(palpite))