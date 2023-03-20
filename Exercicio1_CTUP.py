'''Escreva um  programa em python que leia 3 notas, calcule e imprima a média e o conceito de acordo com a tabela abaixo
- média maior ou igual a 9 - conceito A
- média maior do que 8 e menor do que 8.9 - conceito B
- média maior do que 7 e menor do que 7.9 - conceito C
- média maior do que 6 e menor do que 6.9 - conceito D
- média menor do que 6 - conceito E
Utilize as estruturas condicionais (if-elif-else e mach-case) para enconar a média e imprimir o conceito.
'''
nota1 = int(input('1ª nota: '))
nota2 = int(input('2ª nota: '))
nota3 = int(input('3ª nota: '))
media = (nota1+nota2+nota3)/3

conceito = ''

if media < 6:
    conceito = 'E'
elif media >= 6 and media <= 6.9:
    conceito = 'D'
elif media >= 7 and media <= 7.9:
    conceito = 'C'
elif media >= 8 and media <= 8.9:
    conceito = 'B'
else:
    conceito = 'A'

match conceito:
    case 'A':
        print('Conceito A')
    case 'B':
        print('Conceito B')
    case 'C':
        print('Conceito C')
    case 'D':
        print('Conceito D')
    case 'E':
        print('Conceito E')
        