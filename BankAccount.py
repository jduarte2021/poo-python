class BankAccount:

      def __init__(self, int_rate, balance = 0):
            self.int_rate = int_rate
            self.balance = balance
            self.faltante = 0
            
      
	
      def deposit(self, amount):
            self.balance += amount
            print(f"Ha depositado: {amount} pesos, su saldo final es: {self.balance} pesos")
            return self

      def withdraw(self, amount):
            if self.balance < amount:
                  self.faltante = amount - self.balance
                  print(f"Su saldo no es suficiente, sobrepasa por {self.faltante}\nFondos insuficientes: cobrar una tarifa de $ 5 y deduzca $ 5")
            else:
                  self.balance -= amount
                  print(f"Realizo un retiro de: {amount} pesos, su lado actualizado es de {self.balance}")
            
      
      def display_account_info(self):
            print(f"Saldo final es {self.balance}")
            return self

      def yield_interest(self):
            if self.balance > 0:
                  interes = self.balance * self.int_rate
                  self.balance = self.balance + interes
                  print(f"Su saldo con interes es de: {interes_final}")
            else:
                  print(f"No tiene saldo")


jimmy = BankAccount(0.01,20000)

jimmy.deposit(80000)

jimmy.withdraw(40000)

jimmy.yield_interest()

jimmy.display_account_info()


