
class Tienda:
    
    def __init__ (self, nombre):
        self.nombre = nombre
        self.lista_productos = []



    def add_product (self, new_product): 
        self.lista_productos.append(new_product)
        return self
        
    def sell_product (self,id) :
        # for cod in range(0, len(self.lista_productos)):
        #     id = cod
        #     print(f"¿Cual eliminara?{id}{self.lista_productos}")
        # return self
        pass

    def inflation (self, percent_increase): 
        if percent_increase:
            self.precio += self.precio * (percent_increase / 100)
        else:
            print("No hay cambios")                       
    def set_clearance (self, category, percent_discount): 
        if categoria == category:
            self.precio -= self.precio * (percent_discount / 100)
        else:
            print("No hay cambios, no exite la categoria")
    
    def mostrar_productos(self):
        for producto in self.lista_productos:
            producto.print_info()