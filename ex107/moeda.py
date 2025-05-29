'''
Crie um modulo chamado moeda.py que tenha as funçoes incorporadas aumentar(), diminuir(), e metade()
. Faça tambem um programa que inporte esse modulo e use algumas dessas funçoes 
'''
def aumentar(preço, taxa):
    global res
    res = preço + (preço * taxa/100)
    return res

def diminuir (preço, taxa):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res


