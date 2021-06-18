class Auto:


    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.km = 0
        self.total_autos = 0




    def __str__(self):
        return f"{self.marca} - {self.modelo}"

# Definicion de metodos

    def cuenta_auto(self, amount):
        self.total_autos += amount
        return self

    def retiro_auto(self, amount):
        self.total_autos -= amount
        return self

    def cantidad(self):
        print(
            f"La cantidad de autos {self.marca} {self.modelo} es: {self.total_autos}")

    def auto_nuevo(self, amount):
        self.km += amount
        if self.km >= 10:
            print(
                f"El auto no es nuevo porque tiene {self.km} Kilometros recorridos")
        else:
            print(f"El auto {self.marca} {self.modelo} es Nuevo")


# Creacion de usuarios con sus parametros
japon = Auto("Toyota", "Corolla")
usa = Auto("Ford", "F150")
europa = Auto("Reanult", "Clio")

# Uso de metodos
# japon

kiloj = int(input(f"Introduce Kilometraje {japon.marca} {japon.modelo}: "))
kilou = int(input(f"Introduce Kilometraje: {usa.marca} {usa.modelo}: "))
kiloe = int(
    input(f"Introduce Kilometraje: {europa.marca} {europa.modelo}: "))

japon.cuenta_auto(1)
japon.auto_nuevo(kiloj)
japon.cantidad()

# usa
usa.cuenta_auto(1)
usa.auto_nuevo(kilou)
usa.cantidad()
# europa
europa.cuenta_auto(1)
europa.auto_nuevo(kiloe)
europa.cantidad()


######PRUEBAS DE CODIGO#####
# muestra de saldo final
japon.display_user_balance()
japon.auto_nuevo()
usa.display_user_balance()
europa.display_user_balance()


nombre = input()
print("Hola, " + nombre)
