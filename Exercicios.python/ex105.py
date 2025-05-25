'''
Faça um programa que tenha uma função chamada notas()
que pode receber varias notas de alunos e vai retornar em um dicionario com as seguintes informações
QUANTIDADE DE NOTAS
    A MAIOR NOTA 
        A MENOR NOTA 
            A MEDIA DA TURMA 
                A SITUAÇÃO (OPICIONAL)
'''
def notas(*n, sit=False):
    r = dict()
    r['total'] =  len(n)
    r['maior'] =  max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r

#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)