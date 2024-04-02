import bs4
import requests
import pathlib

directorio = pathlib.Path("c:/Users/Daniel/Desktop/Programación Extra/python/Fotos")


resultado = requests.get("https://www.mastermind.ac/branches/desarrollo")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select(".thumb-container img")
i = 0

for img in imagenes:
    img_guardar = requests.get(img['src']).content
    archivo = open(f"{directorio}/imagen-{i}.jpg", "wb")
    archivo.write(img_guardar)
    archivo.close()

    i += 1
    

# imagen_guardar = requests.get(columna_lateral)
# f = open("mi_imagen.jpg", "wb")
# f.write(imagen_guardar.content)
# f.close()

