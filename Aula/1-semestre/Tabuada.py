'''
Tabuada usando while
'''
tab = int(input('Qual o número escolhido para a tabuada?'))

for nun in range (0,11,1):
    print((str(tab) + " x " + str(nun) + " = " + str(tab*nun)))
    
    
print('Fim!')
