'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
A media de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem mais de 20 anos '''
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0

for p in range(1, 5):
    print('_____________{}° PESSOA_________________' .format(p))
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade:'))
    sex = str(input('Fale seu sexo F femenino (M pra masculino): ')).upper()
    soma_idade = soma_idade + idade
    if p == 1 and sex in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sex in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome 
    if sex in 'Ff' and idade < 20:
        tot_mulher20 = tot_mulher20 + 1
media_idade = soma_idade / 4
print('A media de idade do gupo foi {}' .format(media_idade))
print('O nome do homem mais velho é {} e sua idade é de {}'.format(nome_velho, maior_idade_homem))
print('Ao todo são {} mulhes que tem 20 anos' .format(tot_mulher20))