#Manipulação de Listas com Funções

'''
1) Função para obter o tamanho da lista - tamanho_lista()
2) Função para criar a lista - criar_lista()
3) Função para imprimir a lista - imprimir_lista()
4) Função para imprimir os elementos pares da lista
5) Função para separar os elementos pares da lista
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
    print("---------------------")
    lista = [] #lista vazia
    i = 0
    while i<t:
        n = int(input("Número: "))
        lista.append(n)
        i+=1
    return lista

def imprimir(lista):
    print("*- Emprimir lista -*")
    print("--------------------")
    for i in lista:
        print(f"Elemento: {i}")

def imprimir_par():
    print("*- Imprimir Pares-*")
    print("----------------------")
    for i in lista:
        if i%2 == 0:
            print(f"Elemento: {i}")
            
def imprimir_impares():
    print("*- Imprimir impares-*")
    print("----------------------")
    for i in lista:
        if i%2 != 0:
            print(f"Elemento: {i}")

lista_par = []
def separar_par():
    print("*- Separando elementos Pares -*")
    print("-------------------------------")
    for i in lista:
        if i%2==0:
            lista_par.append(i)
    return lista_impar

lista_impar = []
def separar_impar():
    print("*- Separando elementos Impares -*")
    print("---------------------------------")
    for i in lista:
        if i%2 != 0 :
            lista_impar.append(i)
    return lista_par

def obter_numero():
    print("*- Obtendo Número -*")
    print("-------------------")
    n = int(input("Número:"))
    return n

def verificar_ocorrencia(n,lista):
    print("*- Verificando Ocorrencia de um número na lista -*")
    print("--------------------------------------------------")
    #flag booleana
    achou = False #estado inicial
    for i in lista:
        achou = True
        return achou
    return achou

    

            


#Programa Principal
t = tamanho_lista()
lista = criar_lista(t)
# imprimir(lista)
# imprimir_par()
# imprimir_impares()
separar_par()
imprimir(lista_par)
separar_impar()
imprimir(lista_impar)
n = obter_numero
verificar_ocorrencia(n, lista)