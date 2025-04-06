''' Crie um program que leia varios numeros inteiros pelo teclado, O programa só vai parar quando o usuario digitar 999
que é a condição de parada, no final mostre quantos numeros foram digitados e qual foi a soma entre eles. 
'''
soma = 0
cont = 0
while True:
    n = int(input('Digite um numero inteiro, [999] para encerrar o programa: '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print('A soma dos numeros digitados foi {}' .format(soma))
print('A quantidade de numeros digitados foi de {}' .format(cont))
print('fim')