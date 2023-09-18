''' Dado dois números, verificar se a divisão do primeiro
número pelo segundo é exata (o resto da divisão deve ser
igual a 0). Se for, o programa deve imprimir a mensagem “A
divisão de (número 1) por (número 2) é exata.
'''

nun1 = int(input('Qual será o número a ser dividido? '))
nun2 = int(input('Qual será o número que dividirá? '))
divisao = nun1/nun2

if int(divisao) == divisao:
    print('Esta é uma divisão exata.')
    print(divisao)
else:
    print('Esta é uma divisão inexata.')
    print(divisao)
print('Fim!')
