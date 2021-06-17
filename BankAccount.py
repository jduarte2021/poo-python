class BankAccount:
	def __init__(self, int_rate, balance): # ¡No olvides agregar valores predeterminados para estos parámetros!
		 # su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
                # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
            self.balance = balance
            self.int_rate = int_rate
	
    def deposit(self, amount):
            self.balance += amount
            return self
		# tu código aqui
	def withdraw(self, amount):
            if self.balance < 0:
            self.balance -= amount
            return self
		# tu código aqui
	def display_account_info(self):
		# tu código aqui
            return f"Saldo final es {self.balance}"
	def yield_interest(self):
		# tu código aqui
            pass

