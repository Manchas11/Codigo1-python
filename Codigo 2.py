n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n2:
    c = n1 / n2
    r = n1 % n2

else:
    c = 0
    r = 0

print("El cociente es: ", c)
print("El residuo es: ", r)
