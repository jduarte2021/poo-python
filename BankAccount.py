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

#Usuario 1
jimmy = BankAccount(0.01,20000)
#Usuario2
esteban = BankAccount(0.02,1000)

#Ejecucion de Jimmy
jimmy.deposit(80000).withdraw(40000)

jimmy.yield_interest()
jimmy.display_account_info()

print("#################---Otro Usuario---################")

#Ejecucion de Esteban
esteban.deposit(3000).withdraw(5000)

esteban.yield_interest()
esteban.display_account_info()

