# dicionário
# tem uma estrutura de "(variavel) = {'(key)':(var)}"

dic = {'unidade':1, 'dezena':10, 'centena':100}
dic_2= dict(zip(['primeiro', 'segundo', 'terceiro'], [1,2,3]))
print(dic)#visualização: {'unidade': 1, 'dezena': 10, 'centena': 100}
print(dic_2)#visualização: {'primeiro': 1, 'segundo': 2, 'terceiro': 3} 
#obs:o que foi feito no "dic_2" foi: foi criado dois arrays diferentes, separados em [], com a mesma quantia de elementos, com a método "zip" contatenou os dois arrays e, logo em seguida, o "dict" criou um novo dicionário com os dois arrays criados anteriormente.
#um exemplo do que ocorreu no "dic_2" em etapas.

lista_1 = ['primeiro', 'segundo', 'terceiro']
lista_2 = [1,2,3]
lista_zipada = list(zip(lista_1, lista_2))
# nesta etapa difere do dicionario, o que ocorrre aqui é: após concatenar com o método zip, pedimos ao computador fazer uma lista com as listas concatenadas, isto faz ele criar uma lista de tuplas. Difente de criar um novo dicionario.
lista_zipada_e_dicionario = dict(zip(lista_1,lista_2))

#acessando um elemento do dicionário 

pessoa = {'nome':'Gabriel','altura':1.7,'idade':23}
print(pessoa)#visualização: {'nome': 'Gabriel', 'altura': 1.7, 'idade': 23}
print(pessoa['nome'])#visualização: Gabriel
print(pessoa.get('nome'))#visualização: Gabriel
print(pessoa.get('peso'))#visualização: None
print(pessoa.get('peso','chave não encontrada'))#visualização: 'chave não encontrada'
print(pessoa.get('nome','chave não encontrada'))#visualização: Gabriel
#quando se procura com o get caso ele não encotre, como exemplo o peso acima, ele irá printar a mensagem escolhida, caso ele encontre, como exemplo o nome, ele irá printrar o nome, não a mensagem

#método keys e values

computador = {'CPU':'Intel','RAM':'16gb','SSD':'16gb'}
print(computador)#visualização: {'CPU': 'Intel', 'RAM': '16gb', 'SSD': '16gb'}
print(computador.get('CPU'))#visualização: 'Intel'
print(computador.keys())#visualização: dict_keys(['CPU', 'RAM', 'SSD'])
print(computador.values())#visualização: dict_values(['Intel', '16gb', '16gb'])

for chave in computador.keys():
    print(f'Chave: {chave} e Valor: {computador[chave]}') 
# visualização Cave: CPU e Valor: Intel
# Cave: RAM e Valor: 16gb
# Cave: SSD e Valor: 16gb

for valor in computador.values():
    print(f'Valor: {valor}')
# visualização:
# Valor: Intel
# Valor: 16gb
# Valor: 16gb

notas = {'Python':8, 'Java':9, 'Banco de dados':7}
for nota in notas.values():
    print(f'Nota: {nota}')
# visualização:
# Nota: 8
# Nota: 9
# Nota: 7
