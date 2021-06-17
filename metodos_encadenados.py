class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = 0

    #Definicion de metodos
    #Deposito
    def make_deposit(self, amount):
        self.balance_cuenta += amount
        return self
    #Descuento
    def make_withdrawal(self, amount):
        self.balance_cuenta -= amount
        return self
    #Mostrar balance
    def display_user_balance(self):
        print (f"El usuario: {self.nombre}  Tiene un saldo de: {self.balance_cuenta}" )

    def transfer_money (self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        return self

#Creacion de usuarios con sus parametros
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
jimmy = Usuario("Jimmy Duarte", "jimmy@duarte.com")

#Uso de metodos encadenados
guido.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(50)
monty.make_deposit(1000).make_deposit(1000).make_withdrawal(50).make_withdrawal(50)
jimmy.make_deposit(1000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50)

#uso metodo tranferencia
guido.transfer_money(jimmy,1000)

#muestra de saldo final
guido.display_user_balance()
monty.display_user_balance()
jimmy.display_user_balance()


