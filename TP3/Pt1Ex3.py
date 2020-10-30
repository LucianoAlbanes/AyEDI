import time

## $ python3 esteArchivo.py > Datos.csv  
   
def entrega_billetes_2(monto):
    billete=100
    inc=0
    billete_actual=billete/(10**inc)
    while (monto>0):
        if monto >= billete_actual:
            monto=monto-billete_actual
        else:
            inc=inc+1
            billete_actual=billete/(10**inc)

# Imprimir el promedio de 1000 ejecucciones
def ejecutarPromPrint(monto):
    segundos = float(0)
    for i in range(0, 1000):
        start = time.time()
        entrega_billetes_2(monto)
        end = time.time()
        segundos += (end-start)
    print(f'{monto}, {segundos}') # Capturar esto desde la shell (1000ms=1s)

# Ejecutar en los intervalos pedidos
for i in range(0,100,10):
    ejecutarPromPrint(i)
for i in range(100,1000,100):
    ejecutarPromPrint(i)
for i in range(1000,10000,1000):
    ejecutarPromPrint(i)
for i in range(10000,100000,10000):
    ejecutarPromPrint(i)
for i in range(100000,1100000,100000): # Para inculir 1,000,000
    ejecutarPromPrint(i)
     