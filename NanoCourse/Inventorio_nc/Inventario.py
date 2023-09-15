from NanoCourse.Funcoes.Funcoes_arquivos import chamarMenu, registrar, persistir, exibir

inventario = {}
opcao = chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        print(exibir())
    opcao = chamarMenu()