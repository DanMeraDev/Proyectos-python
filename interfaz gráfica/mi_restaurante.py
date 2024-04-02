from tkinter import *

# iniciar tkinter
aplicacion = Tk()

# tamano de la ventana
aplicacion.geometry('1020x630+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

# titulo de la ventana
aplicacion.title("Restaurante JAD - Sistema de Facturación")

# color de fondo de la ventana
aplicacion.config(bg='burlywood')

# evitar cierre de pantalla
aplicacion.mainloop()