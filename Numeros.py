class Basico:
    x=1
    def __init__(self,numero1,numero2):
        self.num1=numero1
        self.num2=numero2

    def numerosN(self, x):
        for x in range(self.num1):
            print (x)
        return self
    
    def multiplo(self):
        return self.num1%self.num2==0

    def DivisoresNumero(self):
        for i in range(1, self.num1 + 1):
            if self.num1 % i == 0:
                print(i, end=" ")
        return self

    def primo(self):
        for n in range(2, self.num1):
         if self.num1 % n == 0:
            print("No es primo", n, "es divisor")
            return False
        print("Es primo")
        return True
    primo(13) 
    def perfecto(self):

        return
class Intermedio(Basico):

    def __init__(self, n, numero):
            super().__init__(n,numero)

    def numerosN(self): # aplicar polimorfismo
        return

    def factorial(self):
        return

    def fibonacci(self):
        return

    def primosGemelos(self):
        return

    def  amigos(self): 
        return