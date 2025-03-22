a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = a + b

if resultado > 0:
    print("El resultado: ", resultado, "es positivo")
elif resultado < 0:
    print("El resultado: ", resultado, "es negativo")
else:
    print("El resultado: ", resultado, "es cero")