class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):  
        self.result += num
        for num in nums:
            self.result += num
            print(nums)  
        return self

    def subtract(self, num, *nums): 
        self.result -= num
        for num in nums:
            self.result -= num   
        return self
# crear una instruccion:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
# x = md.add(7).add(50,3,9).subtract(2,4).result
# x = md.add(4).add(4,10,2).subtract(6,4).result
# x = md.add(6).add(6,5,1).subtract(3,6).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
