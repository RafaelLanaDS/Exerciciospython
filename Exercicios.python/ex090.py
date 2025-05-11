'''
Faça um programa que leia nome media de um aluno guardando tambem a situação en um dicionario.
No final, mostre o conteudo da estrutura na tela 
'''


aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno['Nome']}: '))


if aluno['Media'] <= 4:
    aluno['situação'] = 'REPROVADO'
elif aluno['Media'] >= 5 and aluno['Media'] < 7.5:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'

print('-=' * 30)
for n, m in aluno.items():
    print(f' - {n} é igual a {m}')