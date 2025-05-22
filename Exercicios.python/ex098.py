'''
Faça um programa que tenha uma função chamada  contador()
quereceba tres parametros,inicio, fim e passo
seu programa tem que realizar tres contagens atraves da função criada 
'''

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' *20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end='', flush=True)
            sleep(0.5)
            cont = cont + p
        print('FIM...')
    else:
        cont = i
        while cont >= f:
            print(f"{cont}" , end='', flush=True)
            sleep(0.5)
            cont = cont - p
        print('FIM...')

#Programa principal
contador(1,  10,  1)
contador(10,  0,  2)
print('-=' *20)
print('agora e sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)