class Calculadora:
    def __init__(self,numero1,numero2):  #metodo constructor
        self.num1=numero1
        self.num2=numero2

    def suma(self):
        return self.num1+self.num2

    def resta(self):
        return self.num1-self.num2

    def multiplicacion(self):
        multi=self.num1*self.num2
        print ("{}*{}={}".format(self.num1,self.num2,multi))

    def division(self):
        return self.num1/self.num2


class calEstandar(Calculadora):

     def __init__(self, numero1, numero2):
            super().__init__(numero1,numero2)    #super se usa para llamar al metodo constructor

     def mutiplicacion(self): # aplicar polimorfismo
         return self.num1*self.num2

     def exponente(self):
         pow(self.num1,self.num2)
         return pow

     def valorAbsoluto(self,numero):
         return abs(numero) #funcion abs sirve para hallar valor absoluto en python


class calCientifica(Calculadora):
    PI=3.1614
    def __init__(self, numero1, numero2):
            super().__init__(numero1,numero2)

    def  circunferencia(self, PI):
         return 2*PI*self.num1

    def areaCirculo(self, PI):
        return PI*self.num1**2

    def areaCuadrado(self):
        return self.num1*self.num1
    def mensaje(men):
        print(men)
