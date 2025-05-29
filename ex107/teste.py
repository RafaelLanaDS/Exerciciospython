import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R$ {moeda.dobro(p)}')
print(f'Aumentando o preço em 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuindo o preço em 10%, temos R$ {moeda.diminuir(p, 10)}')