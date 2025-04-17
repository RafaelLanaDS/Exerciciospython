''' Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km, mostre uma mensagem
dizendo que ele foi multado, a multa vai custar 7 reais por cada km acima do limete. '''

velocidade = float(input('Digite a velocidade atual do veiculo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Vejo ultrapassou o limite permitido de velocidade que é 80Km/h.')
    print('Voce recebera uma multa de {:.2f}' .format(multa))
print('Dirija com segurança !!')