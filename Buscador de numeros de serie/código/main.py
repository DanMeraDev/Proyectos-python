import shutil
from expresionRegular import patron
from datetime import datetime
import os 
from pathlib import Path
import re
import time
import math

# archivo_mover = "C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Herramientas\\Proyecto+Dia+9.zip"
# carpeta_mover = "C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Herramientas\\Proyecto"
# shutil.move(archivo_mover, carpeta_mover)

# shutil.unpack_archive("C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Herramientas\\Proyecto\\Proyecto+Dia+9.zip", "C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Herramientas\\Proyecto", "zip")

# archivo = open("Instrucciones.txt", "r")
# print(archivo.read())
# archivo.close()
def fecha_formato_general(fecha):
    dia = fecha.strftime("%d")
    mes = fecha.strftime("%m")
    anio = fecha.strftime("%y")
    
    return f"{dia}/{mes}/{anio}"
    
directorio = Path("C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Proyecto python\\Buscador de numeros de serie\\Mi_Gran_Directorio")
fecha = datetime.now()
fecha_formato = fecha_formato_general(fecha)
contador_numeros = 0


os.system("cls")
print("-"*52)
print(f"Fecha de búsqueda: {fecha_formato}")
print("")
print("ARCHIVO \tNRO.SERIE")
print("------- \t----------")
inicial = time.time()
for archivo in directorio.glob("**/*"):
    if ".txt" in os.path.basename(archivo):
        texto = open(archivo, "r").read()
        busqueda = re.search(patron, texto)
        if(busqueda):
            print(f"{os.path.basename(archivo)}\t{busqueda.group()}")
            contador_numeros += 1
final = time.time()
duracion = final - inicial
print("")
print(f"Números encontrados: {contador_numeros}")
print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
print("-"*52)