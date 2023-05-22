
veiculos = []

def entrada_modelo ():
    modelo = []
    i = 0
    while i < 5:
        modelo.append (input("Digite o nome do modelo: "))
        i+=1
    return modelo

def entrada_kmL ():
    kmL = []
    i = 0
    while i < 5:
        kmL.append (input("Digite quantos km por litro faz:"))
        i+=1
    return kmL

def entrada_veiculo():
    veiculos.append(modelo, kmL)

modelo = entrada_modelo()
kmL = entrada_kmL()
veiculos = entrada_veiculo()

print(veiculos)