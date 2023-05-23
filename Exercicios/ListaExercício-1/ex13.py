#Fazer um algoritmo que leia três números e imprime o maior deles.

x = float(input("Número 1: "))
y = float(input("Número 2: "))
z = float(input("Número 3: "))

if x > z and x > y:
    print(f"Número {x} é o maior número")
elif z > x and z > y:
    print(f"Número {z} é o maior número")
else:
    print(f"Número {y} é o maior número")