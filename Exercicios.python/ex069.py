'''
Crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa devera perguntar se o usuario quer 
ou não continuar. No final, mostrar
A) quantas pessoas tem mais de 18

B) quantos homens ,foram cadastrados

C) quantas mulheres tem menos de 20
'''
p = 0
total18 = 0
homens = 0
mulher20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    p = p + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('qual seu sexo [F/M]?: ')).strip().upper()[0]
    if idade >= 18:
        total18 = total18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulher20 = mulher20 + 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if  resp == 'N':
        break   
print('Foram entrevistadas {} maiores de idade' .format(total18))
print('No total foram intrevistados {} homens' .format(homens))
print('E temos um total de {} mulher com a idade menor de 20 anos' .format(mulher20))
print('foram {} pessoas intrevistadas' .format(p))    
