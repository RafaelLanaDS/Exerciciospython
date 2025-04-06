''' Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

Aula Anterior
Voltar para Módulo
 '''
num = 0
soma = 0
cont = 0
num = int(input('Digite um numero inteiro e [999 pra sair: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um numero inteiro e [999 pra sair: '))
print('Voce digitou {} numeros e a soma entre ele foi {}' .format(cont, soma))
