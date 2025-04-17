''' Faça um program que leia um frase pelo teclado e mostre:
. quantas veszes aparece a letra "A"
. Em que posição ela aparece a primeira vez
. Em que posição ela aparece na ultima vez '''

frase = str(input('Dgite um frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posição{}. '.format(frase.find('A') +1))
print('A ultima letra A aparceu na posição {}. '.format(frase.rfind('A') +1))