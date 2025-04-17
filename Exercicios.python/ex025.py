''' Crie um progama que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome'''

nome = str(input('Digite seu nome completo: ')).strip() .upper()
print('SILVA' in nome)