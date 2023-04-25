print('Inicio')
d = 0
statusD = 0
statusH = 0
statusM = 0
statusS = 0

while statusH != 1 and statusM != 1 and statusS != 1 and statusD != 1:
    w = input('Defina o dia da semana: ')
    x = int(input('Defina a horario alarme: '))
    y = int(input('Defina o minuto do alarme: '))
    z = int(input('Defina o segundo do alarme: '))

    match statusD:
        case 'Segunda' | 'segunda' | 'Segunda-feira':
            statusD = 1
            d = 2
        case 'Terça':
            statusD = 1
            d = 3
        case 'Quarta':
            statusD = 1
            d = 4
        case 'Quinta':
            statusD = 1
            dia = 5
        case 'Sexta':
            statusD = 1
            dia = 6
        case 'Sabado':
            statusD = 1
            dia = 7
        case 'Domingo':
            statusD = 1
            dia = 1
        case _:
            statusD = 0

    if x > 0 and x < 24:
        statusH = 1
    if y > 0 and y < 60:
        statusM = 1
    if z > 0 and z < 60:
        statusS = 1

while dia < 7:
    h = 0
    while h < 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print(f'{h:02}:{m:02}:{s:02}')
                if d == w and h == x and m == y and s == z:
                    print('_________________________________________________')
                    print('(@.@) ------------------------------------- (@.@)')
                    print('_________________________________________________')
                    break
                s += 1
            if d == w and h == x and m == y:
                break
            m += 1
        if d == w and h == x:
            break
        h += 1
    match dia:
        break
    d += 1
