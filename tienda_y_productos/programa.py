from producto import Producto
from tienda import Tienda
#print(__name__)

# tienda1= Tienda("tienda1")
# producto = tienda1.add_product("manzana")

# print(tienda1)


# print("----------Selecciona Opcion----------")
# input

tienda1 = Tienda("tienda1")

tomate = Producto("Tomates", 500, "Verduras")
lechuga = Producto("Lechuga", 1000, "Verduras")
leche = Producto("Leche", 2000, "Abarrote")

tienda1.add_product(tomate)
tienda1.add_product(lechuga)
tienda1.add_product(leche)

tienda1.mostrar_productos()

tienda1.inflation(10)
