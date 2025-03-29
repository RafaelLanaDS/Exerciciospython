''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
[
Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor: '))
opcao = 0 
while opcao != 5:
    print('''
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa''')
    opcao = int(input('Qual opção quer escolher: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}' .format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('O resiltado de {} x {} é {}' .format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}' .format(n1, n2, maior))
    elif opcao == 4:
        print('Informe um novo valor')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Fizalizando...')
        sleep(2)
    else:
        print('Opção invalida tente novamente')
    print('-=-' * 10)
print('fim do programa')
