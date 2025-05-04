'''
Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista
ja na possição correta de inserção (sem usar sort)
no final mostre a lista ordena na tela
'''
lista = list ()
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    
    if c == 0 or n > lista[-1]: # se for o primeiro valor numero (c == 0;) ou se nao for maior que o ultimo numero da lista
        lista.append(n) # adiciona o numero no final da lista 
        print('Adicionado ao final da lista ')
    else:
        pos = 0 # começa a procurar a posição correta a partir do inicio da lista
        while pos < len(lista): # enquanto nao encontrar a posição correta 
            if n <= lista[pos]: # se n for menor ou igual ao numero maior ou igual 
                lista.insert(pos, n) # insere n antes do numero maior ou igual
                print('Adiciona na posição {} da lista...' .format(pos))
                break
            pos = pos + 1 # vai para aproxima posição 

print('-=' * 30)
print('Os valores digitados em ordem foram {}' .format(lista))