'''Escreva um  programa em python que leia 3 notas, calcule e imprima a média e o conceito de acordo com a tabela abaixo
- média maior ou igual a 9 - conceito A
- média maior do que 8 e menor do que 8.9 - conceito B
- média maior do que 7 e menor do que 7.9 - conceito C
- média maior do que 6 e menor do que 6.9 - conceito D
- média menor do que 6 - conceito E
Utilize as estruturas condicionais (if-elif-else e mach-case) para enconar a média e imprimir o conceito.
'''

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
media = (nota1+nota2+nota3)/3

'''Criar a variavel conceito não e necessário no python, porém, no java e demais necessita a criação da variavel previamente.'''
conceito = ''

if media < 6:
    conceito = 'E'
elif media >= 6 and media < 7:
    conceito = 'D'
elif media >= 7 and media < 8:
    conceito = 'C'
elif media >= 8 and media < 9:
    conceito = 'B'
else:
    conceito = 'A'

match conceito:
    case 'A':
        print('Conceito ', conceito)
        print('Sua média é de ', round(media, 2))
    case 'B':
        print('Conceito ', conceito)
        print('Sua média é de ', round(media, 2))
    case 'C':
        print('Conceito ', conceito)
        print('Sua média é de ', round(media, 2))
    case 'D':
        print('Conceito ', conceito)
        print('Sua média é de ', round(media, 2))
    case 'E':
        print('Conceito ', conceito)
        print('Sua média é de ', round(media, 2))
        