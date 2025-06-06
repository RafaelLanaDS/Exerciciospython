'''
Faça um mini-sistema que utiliza o interactive help do python O usuario vai digitar o comando manual
vai aparecer. Quandoo usario digitar a palavra fim 'FIM', o programa se encerrará. importante: use cores 
'''

from time import sleep

c = (   
        '\033[m'        #0 - sem cor
        '\033[0;30;41m' #1 - vermelho
        '\033[0;30;42m' #2 - verde
        '\033[0;30;43m' #3 - amarelo
        '\033[0;30;44m' #4 - azul
        '\033[0;30;45m' #5 - roxo
        '\033[0;30m'    #6 - branco
    )

def ajuda(com):
    titulo(f'ACESANDO O MANUAL DO COMANDO \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('ATÉ LOGO')