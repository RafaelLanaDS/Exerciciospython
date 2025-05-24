'''
Crie um programa que tenha a função leiaint()
que vai funcionar de forma semelhante a função input
so que vai fazer a validação para ceitar apenas um valor numerico
EX: n = leiaint('digite um numero')
'''


def leiaint(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO digite um numero inteiro valido')
        if ok:
            break
    return valor


#Programa principal 
n = leiaint('Digite um numero: ') # n é uma variavel global ela vai funcionar tanto dentro e fora do DEF
print(f'Voce acabou de digitar o numero {n}')
