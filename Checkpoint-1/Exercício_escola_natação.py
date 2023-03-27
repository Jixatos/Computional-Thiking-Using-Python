idade = int(input('Qual a idade do nadador? '))

categoria = ''

if idade >= 5 and idade <= 7:
    categoria = ('infA')
elif idade >= 8 and idade <= 10:
    categoria = ('infB')
elif idade >= 11 and idade <= 13:
    categoria = ('juvA')
elif idade >= 14 and idade <= 17:
    categoria = ('juvB')
elif idade >= 18:
    categoria = ('sen')
else:
    categoria = ('null')

match categoria:
    case 'infA':
        print('Você entra na categoria infantil A.')
    case 'infB':
        print('Você entra na categoria infantil B.')
    case 'juvA':
        print('Você entra na categoria juvenil A.')
    case 'juvB':
        print('Você entra na categoria juvenil B.')
    case 'sen':
        print('Você entra na categoria Sênior.')
    case 'null':
        print('A criança não tem idade o suficiente para poder nadar.')
