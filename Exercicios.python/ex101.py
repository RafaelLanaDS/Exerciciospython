'''
 Crie um programa que tenha uma função chamada voto() 
 que vai receber como paramentro o ano de nascimento de uma pessoa 
 retornando um valor literal 
 indicando se uma pessoa tem voto
 NEGATIVO, OPICIONAL ou OBRIGATORIO nas eleçoes.
'''
from datetime import date

def voto(nasc):
    '''
    - Você pede o ano de nascimento (nasc) do usuário.
    - A função voto recebe esse ano e calcula a idade.
    - Com base na idade, ela retorna a situação do voto.
    '''
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return(f'Com {idade} anos: NÃO VOTA')

    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPICIONAL'
        
    else:
        return f'com {idade} anos: VOTO OBRIGATORIO'
    

help(voto)

nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))