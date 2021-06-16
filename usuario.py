class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = 0

    #Definicion de metodos
    #Deposito
    def make_deposit(self, amount):
        self.balance_cuenta += amount
    #Descuento
    def make_withdrawal(self, amount):
        self.balance_cuenta -= amount
    #Mostrar balance
    def display_user_balance(self):
        print (f"El usuario: {self.nombre}  Tiene un saldo de: {self.balance_cuenta}" )

    def transfer_money (self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount


guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
jimmy = Usuario("Jimmy Duarte", "jimmy@duarte.com")

guido.make_deposit(1000)
guido.make_deposit(1000)
guido.make_deposit(1000)
guido.make_withdrawal(50)
monty.make_deposit(1000)
monty.make_deposit(1000)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
jimmy.make_deposit(1000)
jimmy.make_withdrawal(50)
jimmy.make_withdrawal(50)
jimmy.make_withdrawal(50)

guido.transfer_money(jimmy,1000)

guido.display_user_balance()
monty.display_user_balance()
jimmy.display_user_balance()


