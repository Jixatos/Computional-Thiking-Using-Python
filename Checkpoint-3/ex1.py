
def entrada_nome():
    nome = input("Digite o nome do atleta: ")
    return nome

def entrada_saltos():
    saltos = []
    i = 0
    if nome != "":
        while i<5: 
            saltos.append(float(input("Digite a distância do salto: ")))
            i+=1
        return saltos
    else:
        sair = True
    return sair

def saida():
    if nome != "":
        print("Atleta: ", nome)
        print("Saltos", saltos)
    else:
        print("Você escolheu sair!")


nome = entrada_nome()
saltos = entrada_saltos()
saida()