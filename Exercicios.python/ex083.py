'''
Crie um programa onde o usuario digite uma expressão qualquer que use parenteses
seu aplicativo devera analisar se a expressão
'''

expr = str (input('Digite  a expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta invalida')