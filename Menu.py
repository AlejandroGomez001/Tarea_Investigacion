""" Menu. Es una clase de 5 opciones:
Menu Principal
1). Calculadora
2). Operación Numeros
3). Tratamiento de Listas
4). Operaciones de  Cadenas
5). Salir
 """
import os 
from calculadora import calEstandar, calCientifica 

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo =titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija Opcion[1...{}]: ".format(len(self.opciones)))
        return opc
opc="0"
while opc!="5":
  os.system("cls")
  men=Menu("Menu Principal", ["1) Calculadora", "2) Numeros","3) Listas","4) Cadenas", "5) Salir"])
  opc=men.menu()
  if opc=="1":
      opc1="0"
      os.system("cls")
      while opc1!="10":
          men1=Menu("Menu Calculadora",["1) Suma","2) Resta", "3) Multiplicacion", "4) Division", "5) Exponente","6) Valor Absoluto","7) Circunferencia" ,"8) Area de un Circulo","9) Area Cuadrado","10) Salir"])
          opc1=men1.menu()
          os.system("cls")
          if opc1=="1":
              print("Suma de dos numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              cal=calEstandar(n1,n2)
              print("{}+{}={}".format(n1,n2,cal.suma()))
              input("Presione una tecla para continuar...")
          elif opc1=="2":
              os.system("cls")
              print("Resta de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              cal=calEstandar(n1,n2)
              print("{}-{}={}".format(n1,n2,cal.resta()))
              input("Presione una tecla para continuar...")
          elif opc1=="3":
              os.system("cls")
              print("Multiplicacion de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              cal=calEstandar(n1,n2)
              print("{}*{}={}".format(n1,n2,cal.multiplicacion()))
              input("Presione una tecla para continuar...")
          elif opc1=="4":
              os.system("cls")
              print("Division de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              cal=calEstandar(n1,n2)
              print("{}/{}={}".format(n1,n2,cal.division()))
              input("Presione una tecla para continuar...")
          elif opc1=="5":
              os.system("cls")
              print("Exponente de Numeros")
              n1=int(input("Ingrese el numero que desea saber su exponente: "))
              n2=int(input("Ingrese el numero de potencia a la que desea elevar el antiguo numero: "))
              cal=calEstandar(n1,n2)
              print("{}^{}={}".format(n1,n2,cal.exponente())) #La funcion pow en python sirve para calcular la potencia de un nnumero
              input("Presione una tecla para continuar...")
          elif opc1=="6":
              os.system("cls")
              print("Valor Absoluto de Numero")
              n1=int(input("Ingrese el numero que desea conocer el valor absoluto: "))
              cal=calEstandar(n1)
              print("El valor absoluto sera: ".format(cal.valorAbsoluto()))
              input("Presione una tecla para continuar...")
          elif opc1=="7":
              os.system("cls")
              print("Circunferencia")
              n1=float(input("Ingrese el radio del circulo: "))
              cal.calCientifica(n1)
              print(cal.circunferencia())
              input("Presione una tecla para continuar...")
          elif opc1=="8":
              os.system("clean")
              print("Area Circulo")
              n1=float(input("Ingrese un numero: "))
              cal.calCientifica(n1)
              print(cal.areaCirculo)
              input("Presione una tecla para continuar...")
          elif opc1 =="9":
              os.system("cls")
              print("Area Cuadrado")
              n1=float(input("Ingrese un numero: "))
              cal.calCientifica(n1)
              print(cal.areaCuadrado)
              input("Presione una tecla para continuar...")
          elif opc1=="10":
              os.system("cls")
              print("Gracias por usar calculadora")
              
  elif opc=="2":
      opc1="0"
      os.system("cls")

      while opc2!="11":
          men2=Menu("Menu Numeros",["1) Presentar los numeros del 1 al n", "2) Sumar los numeros del 1 al n", "3) Multiplo de cualquier numero","4) Presentar los divisores de un numero", "5) Numero Primo", "6) Factorial de cualquier numero ", "7) Fibonacci de una serie de n números", "8) Perfecto", "9) Primos Gemelos", "10)Numero Amigo","11) Salir"])
          opc2=men2.menu()
          os.system("cls")
          if opc1=="1":
              print("Presentar los numeros del 1 al n")
              n1=int(input("Ingrese un numero: "))
              n2=int(input("Ingrese el numero al que desea llegar: "))
              input("Presione una tecla para continuar...")
          elif opc1=="2":
              os.system("cls")
              print("Sumar los numeros del 1 al n")
              n1=int(input("Ingrese un numero: "))
              n2=int(input("Ingrese el numero al que desea llegar: "))
              input("Presione una tecla para continuar...")
          elif opc1=="3":
              os.system("cls")
              print("Multiplo de cualquier numero")
              n1=int(input("Ingrese el primer numero: "))
              input("Presione una tecla para continuar...")
          elif opc1=="4":
              os.system("cls")
              print("Division de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              cal=calEstandar(n1,n2)
              print("{}/{}={}".format(n1,n2,cal.division()))
              input("Presione una tecla para continuar...")
          elif opc1=="5":
              os.system("cls")
              print("Exponente de Numeros")
              n1=int(input("Ingrese el numero que desea saber su exponente: "))
              n2=int(input("Ingrese el numero de potencia a la que desea elevar el antiguo numero: "))
              cal=calEstandar(n1,n2)
              print("{}^{}={}".format(n1,n2,cal.exponente())) #La funcion pow en python sirve para calcular la potencia de un nnumero
              input("Presione una tecla para continuar...")
          elif opc1=="6":
              os.system("cls")
              print("Valor Absoluto de Numero")
              n1=int(input("Ingrese el numero que desea conocer el valor absoluto: "))
              cal=calEstandar(n1)
              print("El valor absoluto sera: ".format(cal.valorAbsoluto()))
              input("Presione una tecla para continuar...")
          elif opc1=="7":
              os.system("cls")
              print("Circunferencia")
              n1=float(input("Ingrese el radio del circulo: "))
              cal.calCientifica(n1)
              print(cal.circunferencia())
              input("Presione una tecla para continuar...")
          elif opc1=="8":
              os.system("clean")
              print("Area Circulo")
              n1=float(input("Ingrese un numero: "))
              cal.calCientifica(n1)
              print(cal.areaCirculo)
              input("Presione una tecla para continuar...")
          elif opc1 =="9":
              os.system("cls")
              print("Area Cuadrado")
              n1=float(input("Ingrese un numero: "))
              cal.calCientifica(n1)
              print(cal.areaCuadrado)
              input("Presione una tecla para continuar...")
          elif opc1=="10":
              os.system("cls")
              print("Gracias por usar calculadora")
  elif opc=="4":
        print("Cadenas")
    
  elif opc=="5":
        print("Gracias por usar el sistema")
  else:
        print("Opcion no valida")

print("Algoritmo finalizado")