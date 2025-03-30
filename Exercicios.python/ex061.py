''' Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> ' .format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM')