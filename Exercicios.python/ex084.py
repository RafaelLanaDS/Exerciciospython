'''
Faça um programa que leia o nome e pesso de varias pessoas guardando tudo em uma lista. no final mostre 
A) quantas pessoas foram cadastradas
B) uma listagem com as pessoas mais pessadas 
C) uma listagem com as pessoas mais leves
'''


pessoas = list ()
princ = list ()
maior = 0 
menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso Kg: ')))

    if len(princ) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    
    princ.append(pessoas[:])
    pessoas.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break

print('-=' * 40 )
print('foram entrevistados {}.' .format(princ))
print('No total participarao {} pessoas.' .format(len(princ)))
print('-=' * 40 )

print('O maior peso foi de {}Kg. Peso de ' .format(maior), end='')
for p in princ:
    if p[1] == maior:
        print('{}' .format({p[0]}), end='')
print()
print('O menor peso foi de {}Kg. Peso de' .format(menor), end='')
for p in princ:
    if p[1] == menor:
        print('{}' .format({p[0]}) , end='')
print()