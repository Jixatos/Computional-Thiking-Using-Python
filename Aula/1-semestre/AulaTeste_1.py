linguagem = input('Linguagem: ')

match linguagem:
    case 'python'|'python':
        print('Modelos IA')
    case 'java'|'Java':
        print('Modelos mobile')
    case 'javascript'|'JavaScript':
        print('Modelos web')
    case 'php'|'PHP':
        print('BackEnd')
    case 'swift'|'Swift':
        print('Mobile IOS')
    case 'c#'|'C#':
        print('Microsoft')
    case _:
        print('Linguagem não especificada')