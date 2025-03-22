def contar_vocales(texto):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for letra in texto:
        if letra == 'a':
            a += 1
        elif letra == 'e':
            e += 1
        elif letra == 'i':
            i += 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1

    print("a:", a)
    print("e:", e)
    print("i:", i)
    print("o:", o)
    print("u:", u)

texto = input("Ingrese una palabra/frase: ")
contar_vocales(texto)