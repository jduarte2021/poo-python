class Producto:
    def __init__ (self, nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def print_info(self): # imprime el nombre del producto, su categoría y su precio.
        print (f"El producto {self.nombre} que tiene la categoria de {self.categoria} tiene un precio de {self.precio}.")

    def update_price(self, percent_change, is_increased = True): 
        
        if is_increased:
            self.precio += self.precio * (percent_change / 100)
        else:
            self.precio -= self.precio * (percent_change / 100)
    