# Generador y decorador

# Generador tickets
def tickets(palabra):
    x = 1
    while 1:
        if len(str(x)) == 1:
            yield f"{palabra}-0{x}"
        else: yield f"{palabra}-{x}"
        x += 1
        
perfumes = tickets("P")
farmacia = tickets("F")
cosmetica = tickets("C")

# Decorador
def informacion_adicional(texto):

    print("="*50)
    print("Su turno es:")
    print(next(texto))
    print("Espere a ser atendid@")
    print("="*50)

