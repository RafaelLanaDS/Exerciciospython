'''
Crie um modulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), e metade()
. Faça tambem um programa que inporte esse modulo e use algumas dessas funçoes 
'''
def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(preço)

def diminuir (preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}' .replace('.', ',')