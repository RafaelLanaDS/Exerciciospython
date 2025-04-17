""" Crie um programa que leia o nome completo de uma pessoa e mostre
. O nome com todas as letras maiusculas
. O nome com todas as letras minusculas
. quantas letras ao todo (sem considerar os espaços) 
. quantas letras tem o primeiro nome """

''' nome = str(input('Digite seu nome completo: '))
frase = (nome.upper()) + (nome.lower())
print(frase)
print(len(nome))
print(frase[0:6]) '''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print("Seu nome em maiusculo é {}" .format(nome.upper()))
print('Seu nome me minuscula é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
