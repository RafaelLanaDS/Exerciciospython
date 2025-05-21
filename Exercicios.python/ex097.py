'''
Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como paramentro e mostre uma mensagem com tamanho adaptavel 
'''
def escreva(msg):
    largura = len(msg) + 4
    print('-' * largura)
    print(f'  {msg}')
    print('-' * largura)



escreva('Rafael Lana de Sousa')
escreva('UNIMAR')
escreva('The Last of Us')
escreva('oi')