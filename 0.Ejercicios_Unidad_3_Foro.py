# EJERCICIO 1:
# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos 
# tienen notas mayores o iguales a 7 y cuántos menores.
def ejercicio1():
    notas=[]
    mayor=0
    menor=0

    for a in range(10):
        valorNota= int(input("Ingrese la nota del estudiante"))

        if valorNota>=7: 
            mayor=mayor+1
        else: 
            menor=menor+1

        notas.append(valorNota)

    print(f"Notas: {notas}")
    print(f"Notas >=7: {mayor}")
    print(f"Notas  <7: {menor}")


# EJERCICIO 2:
# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio 
# de las personas.
def ejercicio2():
    alturas=[]
    continuar=0
    cont=1
    suma=0

    while continuar==0:
        dato= float(input(f"Ingrese la altura de la persona {cont}: "))
        alturas.append(dato)

        seguir=str(input("Desea continuar? S/N "))
        if seguir=="S" or seguir=="s":
            continuar=0
            cont=cont+1
        else:
            continuar=continuar+1

    for n in alturas:
        suma=suma+n

    promedio= suma /len(alturas)

    print()
    print("----------------------------")
    print(f"Altura promedio: {promedio}")
    print("----------------------------")   


# EJERCICIO 3:
# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar 
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados 
# cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá 
# informar el importe que gasta la empresa en sueldos al personal.
def ejercicio3():
    continuar=0
    sueldos=[]
    rango1=0
    rango2=0
    suma=0

    while continuar==0:
        valor=int(input("Digite el sueldo a cobrar: "))

        if valor==-1:
            # -1 para salir del bucle
            continuar=continuar+1

        elif valor<100 or valor>500:
            # Si el valor no esta entre el rango muestra una advertencia
            print("El valor del sueldo solo  puede estar entre $100 y $500.")

        else:

            #Se hace un contador para determinar si el salario digitado estra entre 100 y 300 o si es mayor
            if valor>=100 and valor<=300:
                rango1=rango1+1
            else:
                rango2=rango2+1

            sueldos.append(valor)

    #Se obtiene la sumatoria total de todos los sueldos almacenados en el arreglo
    for sueldo in sueldos:
        suma=suma+sueldo

    print()
    print("-----------------------------------------------------------")
    print(f"Cantidad empleados con sueldos entre $100 y $300: {rango1}")
    print(f"Cantidad empleados con sueldo mayor a $300: {rango2}")
    print(f"Importe total en sueldos: ${suma}")
    print("-----------------------------------------------------------")


# EJERCICIO 4:
# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se 
# ingresan valores por teclado)
def ejercicio4():
    x=11*25
    a=11
    while x>=a:
        print(a)
        a=a+11


# EJERCICIO 5:
# Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
def ejercicio5():
    a=8
    b=1
    x=500

    while x>=a:
        print(f"8x{b} ={a}")
        a=a+8
        b=b+1


# EJERCICIO 6:
# Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
def ejercicio6():
    #Importar random de python para hacer random en numeros
    import random

    lista1=[]
    lista2=[]
    sumalista1=0
    sumalista2=0
    x=1

    while x<=15:
        #Se cargan las listas con numeros aleatorias del 1 al 9
        lista1.append(random.randrange(1, 10))
        lista2.append(random.randrange(1, 10))
        x=x+1

    for lis1 in lista1:
        sumalista1= sumalista1+lis1

    for lis2 in lista2:
        sumalista2= sumalista2+lis2

    print()
    print("-------------------------------------------------------------")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print()
    if sumalista1>sumalista2:
        print(f"Lista 1={sumalista1} es mayor que Lista 2={sumalista2}")
    elif sumalista2>sumalista1:
        print(f"Lista 2={sumalista2} es mayor que Lista 1={sumalista1}")
    elif sumalista2==sumalista1:
        print(f"Lista 1={sumalista1} es igual que Lista 2={sumalista2}")
    print("-------------------------------------------------------------")


# EJERCICIO 7:
# Desarrollar un programa que permita cargar n números enteros y luego nos informe 
# cuántos valores fueron pares y cuántos impares.
# Emplear el operador “%” en la condición de la estructura condicional (este operador 
# retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
#  if valor%2==0: 
def ejercicio7():
    b=1
    listaNumeros=[]
    pares=0
    impares=0

    a= int(input("Cuantos valores quiere cargar? "))

    while a>=b:
        num=int(input(f"Ingrese el valor {b}:"))
    
        if num%2==0:
            pares=pares+1
        else:
            impares=impares+1

        listaNumeros.append(num)
        b=b+1

    print("")
    print("--------------------------------")
    print(f"Numeros ingresados: {listaNumeros}")
    print(f"Cantidad de pares: {pares}")
    print(f"Cantidad de impares: {impares}")


#------------------------------------------------------------------------------------------------
#FOR
#------------------------------------------------------------------------------------------------

# EJERCICIO 8:
# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la 
# medida de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.
def ejercicio8():
    listaTriangulos=[]
    cantidad=0

    a= int(input("Cuantos pares va a ingresar? "))

    for x in range(1,a+1):
        print("////////////////////////////")
        print(f"Triangulo {x}")
        base= int(input("Ingrese la base: "))
        altura= int(input("Ingrese la altura: "))
        superficie=(base*altura)/2

        if superficie>12:
            cantidad=cantidad+1

        listaTriangulos.append([base,altura,superficie])

    print()
    print(f"Triangulos: {listaTriangulos}")
    print(f"Triangulos con superficie mayor a 12: {cantidad}")


# EJERCICIO 9:
# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los 
# últimos 5 valores ingresad
def ejercicio9():
    suma=0
    for x in range(1,11):
        a= int(input(f"Ingrese numero {x}: "))

        if x>5:
            suma=suma+a

    print("----------------------------")
    print(f"Suma ult. 5 numeros: {suma}")
    print("----------------------------")


# EJERCICIO 10:
# Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
def ejercicio10():
    print("Tabla de multiplicar 5:")
    for x in range(1,11):
        print(f"5x{x}={(5*x)}")


# EJERCICIO 11:
# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la 
# tabla de multiplicar del mismo (los primeros 12 términos)
def ejercicio11():
    a= int(input("Ingrese numero para generar tabla de multiplicar: "))

    if a<1 or a>10:
        print("Solo se puede ingresar valores del 1 al 10")
    else:
        print(f"Tabla de multiplicar del {a}:")
        for x in range(1,13):
            print(f"{a}x{x}={(a*x)}")


# EJERCICIO 12: (X)
# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: 
#   equilátero (tres lados iguales), 
#   isósceles(dos lados iguales), 
#   o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.
def ejercicio12():
    contar=0
    conjuntoTriangulo = set()
    triangulos=[]

    equilatero=0
    isosceles=0
    escaleno=0

    a= int(input("Cantidad de triangulos?: "))
    for x in range(1, a+1):
        print("--------------------------")
        print(f"Triangulo {x}:")
        lado1= int(input("Lado 1:"))
        lado2= int(input("Lado 2:"))
        lado3= int(input("Lado 3:"))

        #Uso un conjunto para determinar cuantos valores no repetidos hay
        #Como los conjuntos son inmutables y no admiten valores repetidos pueden servir para el caso de uso de validar.
        conjuntoTriangulo.add(lado1)
        conjuntoTriangulo.add(lado2)
        conjuntoTriangulo.add(lado3)

        #Recorro el conjunto final con los datos para hacer un conteo de sus items
        for b in conjuntoTriangulo:
            contar=contar+1

        #Si los 3 lados son iguales el conjunto solo almacenara al final un valor
        #Si     2 lados son iguales el conjunto solo almacenara al final dos valores
        #Si los 3 lados son diferentes el conjunto solo almacenara al final tres valores
        if contar==1: 
            tipo="equilatero"
            equilatero=equilatero+1

        elif contar==2:
            tipo="isósceles"
            isosceles=isosceles+1

        elif contar==3:
            tipo="escaleno"
            escaleno=escaleno+1

        #Guardo la informacion releavnte en una lista
        triangulos.append([f"Triangulo {x}",tipo])

        #Vacio el conjunto para el siguiente uso y inicializo el contador
        conjuntoTriangulo.clear()
        contar=0

    print()
    print("---------------------------------------------------")
    print(f"triangulos: {triangulos}")
    print(f"equilateros: {equilatero}")
    print(f"isosceles: {isosceles}")
    print(f"escalenos: {escaleno}")
    print("---------------------------------------------------")


#EJERCICIO 13:
# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el 
# plano.Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto 
# cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a 
# procesar.
#     y
#     |
#   2 | 1
# ----------X
#   3 | 4
#     |
#  (x,y)    
# 1(+,+)
# 2(-,+)
# 3(-,-)
# 4(+,-)
def ejercicio13():
    cuad1=[]
    cuad2=[]
    cuad3=[]
    cuad4=[]

    a=int(input("Igrese la cantidad de puntos a procesar: "))

    for b in range(1, a+1):
        print("---------------------------")
        x = int(input("Ingrese cordenadas (X): "))
        y = int(input("Ingrese cordenadas (Y): "))

        if(x>0 and y>0):
            cuad1.append((x,y))
        elif(x<0 and y>0):
            cuad2.append((x,y))
        elif(x<0 and y<0):
            cuad3.append((x,y))
        elif(x>0 and y<0):
            cuad4.append((x,y))

    print("---------------------------------------")
    print(f"Cuadrante 1: {len(cuad1)}")
    print(f"{cuad1}")
    print()
    print(f"Cuadrante 2: {len(cuad2)}")
    print(f"{cuad2}")
    print()
    print(f"Cuadrante 3: {len(cuad3)}")
    print(f"{cuad3}")
    print()
    print(f"Cuadrante 4: {len(cuad4)}")
    print(f"{cuad4}")
    print("---------------------------------------")


#EJERCICIO 14:
# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.
def ejercicio14():
    pos=[]
    neg=[]
    mul=[]

    acu=[]
    sumacu=0

    for a in range(1,11):

        valor= int(input(f"Ingrese el valor {a}: "))

        if(valor>0):
            pos.append(valor)
        elif(valor<0):
            neg.append(valor)

        if(valor%15==0):
            mul.append(valor)
        
        if(valor%2==0):
            acu.append(valor)
            sumacu=sumacu+valor

    print("---------------------")
    print(f"Numeros negativos: {len(neg)}   / {neg}")
    print(f"Numeros positivos: {len(pos)}   / {pos}")
    print(f"Multiplos  de  15: {len(mul)}   / {mul}")
    print(f"Acumulado # pares: {sumacu} / {acu}")    


#EJERCICIO 15:
# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio 
# de edades mayor.
def ejercicio15():
    manSum=0
    tarSum=0
    nocSum=0

    promedios=[]

    print("------------")
    print("Turno Mañana")
    for a in range(1,5+1):
        edades1= int(input(f"Ingrese edad de estudiante {a}:"))
        manSum=manSum+edades1

    print("------------")
    print("Turno Tarde")
    for a in range(1,6+1):
        edades2= int(input(f"Ingrese edad de estudiante {a}:"))
        tarSum=tarSum+edades2

    print("------------")
    print("Turno Noche")
    # son 11
    for a in range(1,11+1):
        edades3= int(input(f"Ingrese edad de estudiante {a}:"))
        nocSum=nocSum+edades3

    #Se guardan los promedios y la clase en una lista
    promedios.append(["Turno Mañana",manSum/5])
    promedios.append(["Turno Tarde",tarSum/6])
    promedios.append(["Turno Noche",nocSum/11])

    # Con una funcion de listas max() se obtiene el valor mas alto
    idx, max_value= max(promedios, key=lambda item: item[1])

    print(f"Turno: {idx}, {max_value}")


#------------------------------------------------------------------------------------------------
#CADENA DE CARACTERES
#------------------------------------------------------------------------------------------------
#EJERCICIO 16:
# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

def ejercicio16():
    texto=str(input("Digite una oración: "))
    vacios= texto.count(" ")
    print(f"Numero de espacios vacios: {vacios}.")


#EJERCICIO 17:
# Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
# para que sea más fácil disponer la condición que verifica que es una vocal.

def ejercicio17():
    texto=str(input("Digite una oración: "))
    minusculas= texto.lower()

    va=minusculas.count("a")
    ve=minusculas.count("e")
    vi=minusculas.count("i")
    vo=minusculas.count("o")
    vu=minusculas.count("u")

    print("----------------------------------")
    print("Cantidad de vocales en la oración:")
    print(f"vocal a: {va}")
    print(f"vocal e: {ve}")
    print(f"vocal i: {vi}")
    print(f"vocal o: {vo}")
    print(f"vocal u: {vu}")
    print("----------------------------------")


#EJERCICIO 18:
# Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
# Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en 
# caso contrario mostrar un mensaje de error

def ejercicio18():
    cadena="Hola que tal como te va esta es tu cadena:"
    texto=str(input("Digite su clave: "))

    if len(texto)<10 or len(texto)>20:
        print("Error: la cedena debe tener una longitud de entre 10 a 20 caracteres")
    else:
        print(cadena +  " " + texto)
