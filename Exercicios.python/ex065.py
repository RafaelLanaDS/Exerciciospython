''' Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

res = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while res in "Ss":
    num = int(input('Digite um numero  inteiro: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar [S/N]: ')).upper().strip()[0] #coloquei em maiuscula, tirei os espaços e pedi o primeira letra perguntada
media = soma / quant
print('A soma entre os numeros foi {}' .format(soma))
print('E media entre os numeros digitados é {:.2f}' .format(media))
print('O maior numero foi {} e menor foi {}' .format(maior, menor))
