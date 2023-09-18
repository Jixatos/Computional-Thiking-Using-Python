# [8:41 AM] Fernando Luiz de Almeida

# 1) Crie uma função semelhante ao exemplo feito em aula, porém, que retorno -1 como resposta para quando não encontrar o valor buscado. Esta versão mantém a coerência do tipo do valor retornado em todas os casos, imprescindível em diversas linguagens de programação

# [8:43 AM] Fernando Luiz de Almeida

# 2) Crie uma função semelhante ao exemplo de aula, porém, que o valor de retorno seja uma lista com os índices de todos os itens iguais ao valor buscado.

# [8:45 AM] Fernando Luiz de Almeida

# 3) Crie uma função semelhante ao exemplo anterior, porém, que a busca parta do último item e avance até o primeiro

lista = [1,2,3,4,5,6,7,8]

def busca(valor, item):
    for i, item in enumerate(lista):
        if item == valor:
            return 1
        else:
            return -1
        
print(busca(2,lista))
