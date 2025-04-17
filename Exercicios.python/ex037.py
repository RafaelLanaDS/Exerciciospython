''' Escreva um programa que leia um numero qualquer e peça para o usuario escolher qual sera a base de conversão
 -1 para binario
 -2 para octal
 -3 para hexadecimal
 '''

num = int(input('Digite um numero inteiro: '))
print('''Escolha umas das bases de conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido para binario é {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}' .format(num, hex(num)[2:]))
else:
    print('Opção invalidade Tente novamente.')