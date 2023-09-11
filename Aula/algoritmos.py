lista = [10,40,30,20,50]
print(lista)
# Atribuição Manual
# temp = lista[1]
# print(lista)

# lista[3] = temp
# print(lsita)

#   Atribuição paralela
# lista [1], lista[3] = lista[3], lista[1]
# print(lista)

lista2 =[40, 30, 20, 50, 10]
def troca(s, i, j):
    s[i], s[j] = s[j], s[i]
    return s

def empurra(lista):
    for i in range(len(lista)- 1):
        if lista[i] > lista[i+1]:
            troca(lista,i,i+1)
    return lista

def bubble_sort(lista):
    n = len(lista)
    while n > 1:
        empurra(lista)
        n-=1
    return lista

print("Bubble sort",bubble_sort(lista2))