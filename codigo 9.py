def calculo(x, y):
    resultado = x + y
    print("La suma es", resultado)

def cuadrado(x):
    return x * x

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

calculo(num1, num2)
print("El cuadrado del primer número que ingresastes es", cuadrado(num1))