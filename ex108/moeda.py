'''
Crie um modulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), e metade()
. Faça tambem um programa que inporte esse modulo e use algumas dessas funçoes 
'''
def aumentar(preço=0, taxa=0):
    global res
    res = preço + (preço * taxa/100)
    return res

def diminuir (preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço=0):
    res = preço * 2
    return res

def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}' .replace('.', ',')