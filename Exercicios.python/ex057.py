'''Faça um programa que leia o sexo de uma pessoa, mais so aceite o valor M ou F. caso esteja errado. peça a digitação novamente ate der um valor correto'''

sexo = str(input('Digite seu sexo [M] para masculino e [F] para femenino: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informação incorreta, Digite novamente por favor !')).strip().upper()[0]
print('Sexo {} salvo com sucesso' .format(sexo))