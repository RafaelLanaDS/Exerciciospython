''' Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando no final, de acordd com a media atingida
 Media abaixo de 5.0: REPROVADO
 Media entre 5.0 e 6.9: RECUPERAÇÃO
 Media 7.0 ou superior: APROVADO
 '''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota1) / 2
if media < 5:
    print('Voce foi reprovado, sua media foi {}' .format(media ))
elif media >= 5 and media < 6.9:
    print('Voce ficou de recuperação, sua media foi {:.1f}'.format(media))
elif media > 7:
    print('Voce foi aprovado,sua media foi {}' .format(media))