# Escreva um program que leia um valor em metros e o exiba em convertido em centimetros e milimetros.

metros = float(input('digite uma distancia em metros: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('a distancia percorrida em {} metros em decimetros {} centimetros {} e em milimetros {}' .format(metros, dm, cm, mm))
km = metros / 1000
hm = metros / 10000
dam = metros / 100000
print('a distancia percorrida em metros foi {}, em km{}, hm {}, e dam {},' .format(metros, km, hm, dam) )