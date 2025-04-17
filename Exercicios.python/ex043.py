''' Desenvolva uma logica que leia o peso e altura de um pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo
 Abaixo de 18.5: Abaixo do peso
 Entre 18.5 e 25: Peso ideal
 25 ate 30: Sobrepeso
 30 ate 40: Obesidade
 Acima de 40: Obesidade morbida
 '''
pesso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('Seu pesso é {} e sua altura é {}' .format(pesso, altura))
imc = pesso / altura ** 2
print('E seu IMC é {:.2f}' .format(imc))
if imc < 18.5:
    print('Voce esta baixo do pesso!!')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no pesso ideial')
elif imc > 25 and imc < 30:
    print('Voce esta com sobrepesso.')
elif imc > 30 and imc < 40:
    print('Voce é esta com obesidade.')
else:
    print('seu imc esta acima de 40, voce esta esta com obesidade morbida.')