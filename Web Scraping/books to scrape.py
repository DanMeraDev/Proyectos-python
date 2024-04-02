import bs4
import requests

# crear url sin numero
url = "https://books.toscrape.com/catalogue/page-{}.html"

# lista de títulos con 4 o 5 
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):
    
    # crear sopa en cada página
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    
    # selección de datos de libros
    libros = sopa.select(".product_pod")
    
    # iterar en los libros
    for libro in libros:
        
        # chequear 4 o 5 estrellas
        if (len(libro.select(".Four")) != 0) | (len(libro.select(".Five")) != 0):
            
            # guardar título en variable
            titulo_libro = libro.select("a")[1]['title']
            
            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)
            

for n in titulos_rating_alto:
    print(n)