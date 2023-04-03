
print('Escolha a operação desejada.')

print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

op = int(input('Qual será a operação desejada? Use apenas números, como no exemplo acima.'))

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))


match op:
    case 1:
        r = n1 + n2
    case 2:
        r = n1 - n2
    case 3:
        r = n1 * n2
    case 4:
        r = n1 / n2
    case _:
        r = 'nd'

        
#Teste usando if
'''
if op == 1:
   r = n1 + n2
elif op == 2
    r = n1 - n2
elif op == 3
    r = n1 * n2
elif op == 4
   r = n1 * n2
else:
    r = 'nd'
'''

#teste antes de imprimir
if r != 'nd':
    print('Resultado: ', r)
else:
    print('Opção é invlálida')
    
