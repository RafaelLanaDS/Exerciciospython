'''Crie um programa que leia uma frase qualquer e diga se ela é um polindroma, desconsiderando os espaços '''

'''def eh_palindromo(frase):
    # Remove espaços e transforma em minúsculas
    frase_limpa = ''.join(frase.lower().split())
    
    # Verifica se a frase é um palíndromo usando um loop for
    tamanho = len(frase_limpa)
    for i in range(tamanho // 2):
        if frase_limpa[i] != frase_limpa[tamanho - i - 1]:
            return False
    return True

# Entrada do usuário
frase = input("Digite uma frase: ")

# Verificação e saída
if eh_palindromo(frase):
    print("A frase {} é um palíndromo!" .format(frase))
else:
    print("A frase {} não é um palíndromo." .format(frase)) '''

frase = str(input('Digite uma frase: ')).strip().upper() # strip remove os espaços da frase 
palavras = frase.split()
junto =''.join(palavras) #join junta todas as palavras sem seus espaços 
inverso =''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')