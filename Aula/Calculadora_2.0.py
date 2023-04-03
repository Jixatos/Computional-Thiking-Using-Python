
print('Escolha a operação desejada.')

while True:
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    op = int(input('Operação: '))
    if op>=1 and op <= 4:
        break

    nun1 = float(input('Número 1: '))
    nun2 = float(input('Número 2: '))

    match op:
        case 1:
            print(f'{nun1} + {nun2}={nun1+nun2:.1f}')
        case 2:
            print(f'{nun1} - {nun2}={nun1-nun2:.1f}')
        case 3:
            print(f'{nun1} * {nun2}={nun1*nun2:.2f}')
        case 4:
            print(f'{nun1} / {nun2}={nun1/nun2:.2f}')
