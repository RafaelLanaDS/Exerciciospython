''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
 sua cotegoria, de acordo com a idade
 Ate 9 anos MIRIN
 Ate 14 anos INFANTIL
 Ate 19 anos JUNIOR
 Ate 20 anos SENIOR
 Acima MASTER'''

from datetime import date

atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print('Voce nasceu no ano {}, e sua idade é {} anos'.format(nascimento, idade))
if idade <= 9:
    print('Sua categoria é MIRIN')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print('Sua categoria é SENIOR')
else:
    print('A sua categoria é MASTER')