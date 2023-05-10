equipamentos = []
valores = []
seriais = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: ")),
  valores.append(float(input("Valor: "))),
  seriais.append(int(input("Número Serial: "))),
  resposta = input("Digite 'S' para continuar: ").upper()

busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])
    
# Todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo
# período) de 10%. Monte o código que seria responsável por alterar o valor de todos os
# equipamentos “impressora”
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
  if depreciacao==equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])
    
# Um equipamento com um determinado número serial foi danificado e será descartado.
# Precisamos eliminar esse equipamento. Dica: para eliminar um item de uma lista, você utilizará o
# Icomando “del”. Exemplo: del lista[<indice>]|
serial=("Qual o número de série do equipamento que deseja deletar?\n")
for indice in range(0,len(equipamentos)):
    if seriais[indice]==serial:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]
        break

