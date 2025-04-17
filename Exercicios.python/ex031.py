''' desenvolva um programa que pergunte a distancia de uma viagem em km calcule o preço da passagem cobrando 0.50 por km
 para viagens de ate 200km e 0.45 para viagens mais longas '''

distancia = float(input('Qual foi a distancia percorrida em km: '))

if distancia <= 200:
    print('Sua viagem custara {}' .format(distancia * 0.50))
elif distancia > 200:
    print('Sua viagem custara {}' .format(distancia * 0.45))