''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
 - se ele ainda vai se alistar
 - se é a hora de se alistar
 - se ja passou do tempo de se alistar
 Seu programa tambem deve mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year #qual o ano de hoje ?
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}' .format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}' .format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado a {} anos' .format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}' .format(ano))