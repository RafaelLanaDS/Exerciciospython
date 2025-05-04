'''
Crie um programa que vai ler varios numeros e colocar em uma lista
depois crie duas listas extras que vão conter apenas valores pares e os valores impares digitados 
no final, mostre o conteudo das tres listas geradas. 
'''

valores = list ()
par = list ()
inp = list ()
while True:
    numeros = int(input('Digite um valor: '))
    valores.append(numeros) #Adicione o número digitado na variavel (numeros5s) à lista chamada valores
    if numeros %2 == 0:
        par.append(numeros)
    else:
        inp.append(numeros)

    resp = ' '
    while  resp not in 'SN':
        resp = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Valores da lista {valores}')
print('Os valores pares foram {}' .format(par))
print('E os valores impares foram {}' .format(inp))