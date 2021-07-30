""" Menu. Es una clase de 5 opciones:
Menu Principal
1). Calculadora
2). Operación Numeros
3). Tratamiento de Listas
4). Operaciones de  Cadenas
5). Salir
 """
import math
import os 
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
      while opc1!="9":
          men1=Menu("Menu Calculadora",["1) Suma","2) Resta", "3) Multiplicacion", "4) Division", "5) Exponente","6) Valor Absoluto","7) Circunferencia y Area de un Circulo","8) Area Cuadrado","9) Salir"])
          opc1=men1.menu()
          if opc1=="1":
              os.system("cls")
              print("Suma de dos numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              print("La suma es: ",n1+n2)
              input("Presione una tecla para continuar...")
          elif opc1=="2":
              os.system("cls")
              print("Resta de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              print("La resta es: ",n1-n2)
              input("Presione una tecla para continuar...")
          elif opc1=="3":
              os.system("cls")
              print("Multiplicacion de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              print("La multiplicacion es: ",n1*n2)
              input("Presione una tecla para continuar...")
          elif opc1=="4":
              os.system("cls")
              print("Division de Numeros")
              n1=int(input("Ingrese el primer numero: "))
              n2=int(input("Ingrese el segundo numero: "))
              print("La division es: ",n1/n2)
              input("Presione una tecla para continuar...")
          elif opc1=="5":
              os.system("cls")
              print("Exponente de Numeros")
              n1=int(input("Ingrese el numero que desea saber su exponente: "))
              n2=int(input("Ingrese el numero de potencia a la que desea elevar el antiguo numero: "))
              print("La potencia del numero ",n1, "es: ",pow(n1,n2)) #La funcion pow en python sirve para calcular la potencia de un nnumero
              input("Presione una tecla para continuar...")
          elif opc1=="6":
              os.system("cls")
              print("Valor Absoluto de Numero")
              n1=int(input("Ingrese el numero que desea conocer el valor absoluto: "))
              print("El valor absoluto del numero ",n1, "es: ",(abs(n1)))
              input("Presione una tecla para continuar...")
          elif opc1=="7":
              os.system("cls")
              print("Circunferencia y Area de un circulo")
              n1=float(input("Ingrese el radio del circulo: "))
              circunferencia=2*math.pi*n1
              area=math.pi*n1**2
              roundarea= round(area,2)        #La funcion round sirve para redondear numeros con gran cantidad de decimales
              roundcircu= round(circunferencia,2)
              print("La circunferencia del circulo sera: ", roundcircu, "y el area sera: ",roundarea)
              input("Presione una tecla para continuar...")
          elif opc1=="8":
              os.system("cls")
              print("Area Cuadrado")
              n1=int(input("Ingrese el valor de un lado del cuadrado: "))
              print("El area del cuadrado es: ",n1*n1)
              input("Presione una tecla para continuar...")
          elif opc1=="9":
              os.system("cls")
              print("Gracias por usar calculadora")
              
  elif opc=="2":
     men2=Menu("Menu Numeros",["1) Perfecto", "2) Primo", "3) Salir"])
     opc2=men2.menu()
     if opc2=="1":
        print("Numeros Perfectos")
        num=int(input("Ingrese un numero: "))
        # Llamar el metodo perfecto
        print("El numero es perfecto")
  elif opc=="3":
        print("Listas")

  elif opc=="4":
        print("Cadenas")
    
  elif opc=="5":
        print("Gracias por usar el sistema")
  else:
        print("Opcion no valida")

print("Algoritmo finalizado")