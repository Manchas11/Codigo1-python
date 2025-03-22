consumo = float(input("Ingresa el consumo: "))

if consumo <= 100:
    descuento = consumo * 0.10
elif consumo <= 200:
    descuento = consumo * 0.20
elif consumo <= 300:
    descuento = consumo * 0.30
else:
    print("Consumo invalido") 

consumo_descuento = consumo - descuento  
    
iva = consumo_descuento * 0.16 

total_pagar = consumo_descuento + iva
    
print("Consumo: ", consumo)
print("Descuento: ", descuento)
print("impuesto: ", iva)
print("Total a pagar: ", total_pagar)