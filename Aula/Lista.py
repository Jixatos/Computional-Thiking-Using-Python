#Manipulação de Listas com Funções

'''
1) Função para obter o tamanho da lista - tamanho_lista()
2) Função para criar a lista - criar_lista()
3) Função para imprimir a lista - imprimir_lista()
4) Função para imprimir os elementos pares da lista
5) Função para separar os elementos impares da lista
7) Função para separar os elementos impares da lista
8) Função que verifica a ocorrencia de um determinado número
9) Função que obtem um número
'''

def tamanho_lista():
    print("*- Tamanho da lista -*")
    print("----------------------")
    return int(input("Tamanho: "))

def criar_lista(t):
    print("*- Criar uma lista -*")
    print("----------------------")
    lista = [] #lista vazia
    i = 0
    while i<t:
        n = int(input("Número: "))
        lista.append(n)
        i+=1
    return lista

def imprimir(lista):
    print("*- Emprimir uma lista -*")
    print("----------------------")
    for i in lista:
        print(f"Elemento: {i}")

def imprimir_par():
    print("*- Números Pares-*")
    print("----------------------")
    for i in lista:
        if i%2 == 0:
            print(f"Elemento: {i}")
            
def imprimir_impares():
    print("*- Números impares-*")
    print("----------------------")
    for i in lista:
        if i%2!=0:
            print(f"Elemento: {i}")

def separar_par():
    print("*- Separar Pares -*")
    print("----------------------")
    for i in lista:
        if i%2==0:
            lista_par = []
            lista_par.append(i)
            print(f"Números pares: {i}")
            
def separar_impar():
    print("*- Separar Impares -*")
    print("----------------------")
    for i in lista:
        if i%2!=0:
            lista_par = []
            lista_par.append(i)
            print(f"Números impares: {i}")
            


#Programa Principal
t = tamanho_lista()
lista = criar_lista(t)
imprimir(lista)
# imprimir_par()
# imprimir_impares()
separar_par()
separar_impar()
