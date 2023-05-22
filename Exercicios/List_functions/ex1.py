# Escreva uma função que receba uma lista de números inteiros como parâmetro e
# retorna a soma de todos os elementos

def max ():
    m = int(input("Digite o maximo da lista: "))
    return m

def lista_int (m):
    ints = []
    i = 0
    while i<m:
        ints.append(int(input("Digite o número que deseja adicionar à lista: ")))
        i+=1
    return ints

def imprimir_todos(m):
    for i in m:
        print(f"Número: {i}")
        i+=1

soma = 0
def soma(lista_int):
    for i in lista_int:
        soma = soma + i
        i+=1
    return soma

m = max()
ints = lista_int(m)
imprimir_todos(ints)

soma(lista_int)
print(soma)