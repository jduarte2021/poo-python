
class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.cuenta = BankAccount(0.01, 0)

class BankAccount:

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        self.faltante = 0


            
	# Metodo para hacer deposito
    def deposit(self, amount):
            self.balance += amount
            print(f"Ha depositado: {amount} pesos, su saldo final es: {self.balance} pesos")
            return self
    # Metodo para hacer retiro
    def withdraw(self, amount):
            if self.balance < amount:
                self.faltante = amount - self.balance
                print(f"Su saldo no es suficiente, sobrepasa por {self.faltante}\nFondos insuficientes: cobrar una tarifa de $ 5 y deduzca $ 5")
            else:
                self.balance -= amount
                print(f"Realizo un retiro de: {amount} pesos, su saldo actualizado es de {self.balance}")
            
        # Metodo para mostrar balance
    def display_account_info(self):
        print(f"Saldo final es {self.balance}")
        return self
    # Metodo para sumar interes
    def yield_interest(self):
        if self.balance > 0:
                self.balance += self.balance * self.int_rate
                #interes_final = self.balance + interes
                print(f"Su saldo con interes es de: {self.balance}")
        else:
                print(f"No tiene saldo")


        

#Creacion de usuarios con sus parametros
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
jimmy = Usuario("Jimmy Duarte", "jimmy@duarte.com")

jimmy.cuenta.deposit(1000).withdraw(500)
jimmy.cuenta.yield_interest()