''' Crie um programa que leia a nome de uma cidade e  diga se ela começa ou nao com o nome 'SANTO' '''

''' cidade = input("Digite o nome da cidade: ").strip().upper()

resultado = cidade.startswith("SANTO") * "A cidade começa com 'SANTO'." + (not cidade.startswith("SANTO")) * "A cidade NÃO começa com 'SANTO'."

print(resultado) '''

cid = str(input('Digite em que cidade voce nasceu: ')).strip() .upper()
print(cid[:5] == 'SANTO')