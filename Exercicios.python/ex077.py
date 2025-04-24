'''
Crie um programa que tenha uma tupla com vários palavras(não usar acentos). Depois disso, voce deve mostrar, para cada palavra, quais são vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in palavras:
    print('\nNa palavra {} temos'.format(c.upper()), end=' ')
    for letra in c:
        if letra.lower()  in 'aeiou':
            print(letra, end=' ')
        

