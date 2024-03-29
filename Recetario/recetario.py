from pathlib import Path
from os import system

import os 
recetario = Path("C:\\Users\\Daniel\\Desktop\\Programación Extra\\python\\Proyectos python")
carpeta_recetas = os.path.basename(recetario)
bucle = 1
def continuacionProceso():
    print()
    input("Presiona cualquier tecla para continuar con el proceso \n")
    system("cls")
    
def elegirCategoria():
    system("cls")
    print("Categorias: \n")
    for carpeta in recetario.glob("*"):
        print("-",os.path.basename(carpeta))
    print()
    categoria = input("Elige una categoria: ")
    system("cls")
    
    return recetario / categoria
      
def elegirRecetas(categoria):
    recetas = []
    print(f"Recetas de {os.path.basename(categoria)}:\n")
    for receta in categoria.glob("*.txt"):
        print("-", receta.stem)
        recetas.append(receta.name)
    print()
    return recetas
system("cls")
while bucle:
    print("------------------------------------")
    print("Bienvenido al recetario Python!")
    print("Las recetas se encuentran en la carpeta", carpeta_recetas)
    print(f"La carpeta {carpeta_recetas} se encuentra ubicada en la ruta absoluta:", recetario)
    print("------------------------------------")
    recetas_cantidad = 0
    for txt in recetario.glob("**/*.txt"):
        recetas_cantidad += 1
    print(f"Hay un total de {recetas_cantidad} recetas")
    print("------------------------------------")
    print("Ingresa una opción para el recetario")
    print("[1] - Leer receta")
    print("[2] - Crear receta")
    print("[3] - Crear categoría")
    print("[4] - Eliminar receta")
    print("[5] - Eliminar categoría")
    print("[6] - Finalizar programa")
    print("------------------------------------")
    numero = int(input())
    print("------------------------------------")
    match numero:
        case 1:
            categoria = elegirCategoria()
            lista_recetas = elegirRecetas(categoria)
            receta_leer = input("Ingresa la receta que quieres leer:\n")
            archivo_leer = open(f"{categoria/receta_leer}.txt")
            system("cls")
            print("Receta:")
            print(archivo_leer.read())
            continuacionProceso()
        case 2:
            categoria = elegirCategoria()
            print(f"Entraste a la carpeta de {os.path.basename(categoria)}")
            nombre_receta = input("Ingresa el nombre de la receta que deseas crear: ")
            contenido_receta = input("Ingresa el contenido de la receta:\n")
            archivo_creado = open(f"{categoria/nombre_receta}.txt", "w")
            archivo_creado.write(contenido_receta)
            print("Receta creada exitosamente")
        case 3:
            categoria_crear = input("Ingresa el nombre de la categoría que deseas crear: ")
            os.makedirs(recetario/categoria_crear)
            print(f"Categoría {os.path.basename(recetario/categoria_crear)} creada exitosamente")
        case 4: 
            categoria = elegirCategoria()
            lista_recetas = elegirRecetas(categoria)
            print()
            archivo_borrar = input("Elige la receta que deseas borrar: ")
            os.remove(f"{categoria/archivo_borrar}.txt")
            print("Receta borrada exitosamente")
        case 5:
            categoria = elegirCategoria()
            os.rmdir(categoria)
            print("Categoría borrada exitosamente")
        case 6:
            bucle = 0
            system("cls")
            print("El programa a finalizado exitosamente")
    

    
