idiomas = ["Árabe", "Ingles", "Fracés", "Español"]
indice = 0
for idioma in idiomas:
    print("Este idioma está en la lista: " + idiomas[indice])
    indice += 1

prueba = "Python"
cadena = prueba
for caracter in cadena: 
    print(caracter)

for x in range(5):
    print(x)
else:
    print("Fin del bucle")

for x in range(5):
    if x == 3:
        break
    print (x)