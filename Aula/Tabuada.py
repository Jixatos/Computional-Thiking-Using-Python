'''
Tabuada usando while
'''
nun = int(input('Qual o número escolhido para a tabuada?'))
mult = 1

while mult <= 10:
    print(f'{nun} * {mult} = {nun*mult}')
    mult += 1

print('Fim!')
