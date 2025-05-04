
teste = list ()
teste.append('Rafael')
teste.append(22)

galera = list()
galera.append(teste[:])
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])



#galera = [['Rafael', 22], ['Jessica', 30], ['Rafaela', 26]]
#for p in galera: # Para cada pessoa em galera 
    #print(p)
    #print(p[0])
    #print(p[1])

#print(galera[0][0])
#print(galera[1][1])
#print(galera[2])
#print(galera[0][1])


galera = list () 
dado = list ()
totmaior = 0
totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Faz uma copia da lista (dado) NÃO ESQUECER OS [:] = ELE QUE CRIA A COPIA DA LISTA 
    dado.clear() # exclui a lista dados para não dar divergencia no print abaixo
#print(galera)

# QUERO MOSTRAR AS PESSOAS COM MAIS DE 21 ANSOS 
for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade.' .format(p[0]))
        totmaior = totmaior + 1
    else:
        print('{} é menor de idade ' .format(p[0]))
        totmenor = totmenor + 1
print('Temos {} maiores e {} menores de idade.' .format(totmaior,  totmenor))