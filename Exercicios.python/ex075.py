'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla,no final mostre 
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
lista = ()
for c in range(0,4):
    numero = int(input('Digite um numero: '))
    lista = lista + (numero,) # se nao colocar a virgula depois do numero da erro
print('-=' * 10)

print('Os numeros digitados foram {}' .format(lista))
print('-=' * 10)

print('O valor 9 apareceu {} vezes' .format(lista.count(9))) # count ira mostrar quantas vezes o nove foi digitado
print('-=' * 10)

if 3 in lista:
    print('O valor 3 apareceu na {}ª possição ' .format(lista.index(3)+1))
else:
    print('O valor tres não foi digitado')
print('-=' * 10)

for n in lista:
    if n % 2 == 0:
        print('os valores pares digitados foram {}' .format(n))
print('-=' * 10)
print('Fim do exercicio')