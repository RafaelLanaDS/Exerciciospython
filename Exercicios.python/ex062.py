'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print('{} -> ' .format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais ?: '))
print('Progessão finalizada com {} termos mostrados' .format(total))