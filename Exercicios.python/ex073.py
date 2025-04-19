'''
Crie uma tupla preechida com os primeiros colocados da tabela do campeonato brasiliero de futebol, na ordem de colocação depois mostre

a) os primeiros times

b) os ultimos 4 colocaods

c) times em ordem alfabetica

d) em que posição esta o time da mirasol

'''

times = 'Flamengo','Palmeiras','Fluminense','Ceará Sporting','Cruzeiro','Red Bull','Vasco da Gama','Juventude','Mirasol','Internacional','Botafogo','Fortaleza','Santos','Corinthias','EC Vitoria','São Paulo','Gremio','Bahia','Atletico-MG','Sport Recife'

print(times)
print('-=' * 20)

print('Fase de grupos da CONMEBOL Libertadores = ' ,times[0:4])
print('-=' * 20)

print('Rebaixamento' , times[-4:])
print('-=' * 20)

print(sorted(times))
print('-=' * 20)

print('O mirasol esta na {} posição' .format(times.index("Mirasol")))
print('-=' * 20)

for cont in range(0, len(times)):
    print('posição de cada time {} na posição {}' .format(times[cont], cont))  


