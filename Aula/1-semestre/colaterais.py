# metódo fromkeys()

listaChaves = ['1chaves1', 'chaves2', 'chaves3']
valor = 0
dictionary = dict.fromkeys(listaChaves, valor)
#print(listaChaves)
#print(dictionary)

lista = ['Pedro', 25, 123, 321, 'abcde', 1234, 4321]
d = {'a1': lista}

# exemplo em função
def teste(a,b,c):
    print(f'a:{a} | b:{b} | c:{c}')
lista = [1,'banana', True]

# teste(lista[0], lista[1], lista[2]) - forma manual
teste(*lista) # forma simplificada

# exemplo 2
def teste2(n, s):
    n = n + 2
    s[0] = s[0] + 1
    return

n1 = 1
lista2 = [1]

print(teste2(n1, lista2))
print('fim')

# Função COM efeito colateral
def converte1(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[1])

# Função SEM efeito colateral
def converte2(lista):
    novaLista = []
    for item in lista:
        novaLista.append(int(item))
    return novaLista

#Principal
numeros1 = ['10', '20', '30', '40']
numeros2 = ['10', '20', '30', '40']
converte1(numeros1)
numeros3 = converte2(numeros2)

print(numeros1)
print(numeros2)
print(numeros3)

# Exemplo
def funcao(z,y,x):
    print(f'a:{z} | b:{y} | c:{x}')

regulagem = {'max':10, 'meio':5, 'min':0}
funcao(**regulagem)







