def mes_en_letras(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        return "Número de mes inválido"

numero_mes = int(input("Introduce el número del mes del 1 al 12: "))
print(mes_en_letras(numero_mes))
