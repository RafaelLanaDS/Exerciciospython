''' 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso. De zero ate vinte 
seu programa devera ler um numero pelo teclado entre (0 a 20) e mostralo por extenso.
'''

cont = 'zero', 'um', 'dois', 'tres', 'quantro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'quatorce', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


while True:
    
    digite = int(input('Digite um numero de 0 a 20: '))
    if 0 <=  digite <= 20:
        print('O numero digitado foi {}' .format(cont[digite]))
    else:
        print('Numero invalido')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
        
    
        