from os import system

import random

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    numero_cuenta = random.randint(2000, 3000)
    balance = 0
        
    def depositar(self, cantidad):
        self.balance += cantidad
        print("Monto depositado efectivamente")
        
    def retirar(self, cantidad):
        if (self.balance >= cantidad):
            self.balance -= cantidad  
            print("Monto retirado efectivamente")
        else: print("Fondos insuficientes para realizar la transacción")
        
    def __str__(self):
        return f"""
        {"-"*30}
        {self.nombre} {self.apellido} usted tiene ${self.balance}
        N. Cuenta: {self.numero_cuenta}
        {"-"*30}
        """
    
system("cls")
print("*"*50)
print("Bienvenido al Banco JAD Development")
print("Ingresa tus datos para crear una cuenta")
nombre_cuenta = input("Ingresa tu nombre: ")
apellido_cuenta = input("Ingresa tu apellido: ")
cliente1 = Cliente(nombre_cuenta, apellido_cuenta)
print(cliente1)
bucle = 1

while bucle:
    print("*"*50)
    print("Que acción desea realizar")
    print("Para realizar un depósito ingrese [1]")
    print("Para realizar un retiro ingrese [2]")
    print("Para cancelar transacción ingrese [3]")
    print("*"*50)
    
    numero = input()

    match numero:
        case "1":
            cantidad = int(input("Ingrese el monto que desea depositar\n"))
            system("cls")            
            cliente1.depositar(cantidad)
            print(cliente1)
        case "2":
            cantidad = int(input("Ingrese el monto que desea retirar\n"))
            system("cls")
            cliente1.retirar(cantidad)
            print(cliente1)
        case "3":
            bucle = 0
            system("cls")
            print(cliente1)
            print("Saliendo del programa...")


    