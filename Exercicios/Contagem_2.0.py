'''
Contagem de números positivos e negativos
'''
min = int(input('Qual o ínicio? '))
max = int(input('Qual o final? '))

if min <= max:
    while min <= max:
        print(min)
        min+=1
else:
    while min >= max:
        print(min)
        min+=-1

print('O valor do min é',min)