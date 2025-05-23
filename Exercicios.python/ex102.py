'''
Crie um programa que tenha uma função chamada fatorial()
que recebe dois parametros
O primeiro que indique o numero a calcular 
O outro chamado SHOW que sera um valor logico (opicional) indicando se será mostrado ou não na tela o processo de calculo do fatorial 
'''

def fatorial(n, show=False):
    """
      
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#programa principal
print(fatorial(5, show=True))