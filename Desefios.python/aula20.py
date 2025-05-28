def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#programa principal
soma(b=4, a=5)
soma(7, 4)

def contador(* num):
    print(num)

contador (1, 2, 3, 4)
contador (7, 5, 6)
contador (9, 1, 2, 9, 2, 4, 3)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos = pos + 1 


valores = [1, 6, 8, 7, 4]
dobra(valores)
print(valores)