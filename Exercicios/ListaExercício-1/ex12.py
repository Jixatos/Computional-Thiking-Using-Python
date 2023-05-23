#  Fazer um algoritmo que leia dois números L e R. O programa deve verificar a maior área entre um quadrado de lado L e um círculo de raio R. Imprimir na tela qual o maior: "Quadrado" ou "Círculo".

l = float(input("Digite o lado L para calcular a área do quadrado: "))
r = float(input("Digite o raio R para calcular a área do circulo: "))

areaC = 2*3.14*r
areaQ = l*l

if areaC > areaQ:
    print(f"A área do circulo {areaC} é maior do que a área do quadrado {areaQ}")
else:
    print(f"A área do quadrado {areaQ} é maior que a área do círculoa {areaC}") 