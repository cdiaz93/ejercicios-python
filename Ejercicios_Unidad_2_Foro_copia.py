# 1. Leer un número entero y determinar si es un número terminado en 4.
# 
def punto0():
    print("In Learning Github sapbee")
    print("Linked In")
    print("Linked In 2")

def punto1():
    entrada= str(input("Digite un numero: "))

    longitud = len(entrada)
    ultimo = entrada[longitud-1]

    if (ultimo==4):
        print(f"el numero {entrada,} termina en 4")
    else:
        print(f"el numero {entrada}, NO termina en 4")

# 2. Leer un número entero y determinar si tiene 3 dígitos. 
def punto2():
    entrada= int(input("Digite un numero: "))
    convertir=str(entrada)
    longitud = len(convertir)

    if longitud==3:
        print("El numero tiene 3 digitos")
    else:
        print("El numero no tiene 3 digitos")

# 3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares. 
def punto3():
    entrada= int(input("Digite un numero de 2 digitos: "))
    convertir=str(entrada)
    primer = int(convertir[0])
    ultimo = int(convertir[1])

    if primer%2==0 and ultimo%2==0:
        print(f"Los numeros: {primer}, y {ultimo} son pares")
    else:
        print("Ambos numeros no son pares")



# 4. Leer un número entero de dos dígitos menor que 20 y determinar si es primo. 

#ANOTACAIONES:
#R/para saber si un numero es primo: (n-1)! + 1
#factorial:(!)
#el resultado final de la formula al dividirlo por el numero que se evaluara si es primo debe dar un numero entero.
# función built-in (funcion matematicas incluidas en python)
def punto4():
    from math import factorial

    continuar=0
    while continuar==0:
        num= int(input("Digite un numero: "))

        if(num>20 or num<1):
            print("El numero ingresado debe estar en un rango de 1-19")
        else:
            formula=factorial((num-1)) +1
            if formula%num==0: 
                print("El numero es primo")
            else:
                print("El numero no es primo")
        
        preg= str(input("Contuniar? S/N: "))
        if preg=="S" or preg=="s":
            continuar=0
        else:
            continuar=1

 
# 5. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo. 
def funcion5():
    from math import factorial

    continuar=0
    while continuar==0:
        num= int(input("Digite un numero de 2 digitos: "))

        if num<0:
            print("El numero es negativo")
        else:
            formula=factorial((num-1)) +1

            if formula%num==0: 
                print("El numero es primo")
            else:
                print("El numero no es primo")

        #Bucle de continuacion
        preg= str(input("Contuniar? S/N: "))
        if preg=="S" or preg=="s":
            continuar=0
        else:
            continuar=1


# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales. 
def funcion6():
    num= str(input("Digite un numero de 2 digitos: "))
    if len(num)==2:
        prim= num[0]
        ulti= num[1]

        validar = prim==ulti
        
        if validar:
            print("Los numeros son iguales")
        else:
            print("Los numeros NO son iguales")
    else:
        print("Solo puede ingresar numeros de 2 digitos")



# 7. Leer dos números enteros y determinar cuál es el mayor. 
def funcion7():
    num1= str(input("Digite 1er numero: "))
    num2= str(input("Digite 2do numero: "))
    maximo= max(num1, num2)

    print(f"El numero mayor es: {maximo}")


# 8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos. 
def funcion8():
    num1= str(input("Digite 1er numero: "))
    num2= str(input("Digite 2do numero: "))

    if len(num1)>2 or len(num2)>2:
        print("Los campos deben tener como maximo 2 digitos")
    else:
        suma= int(num1[0]) + int(num1[1]) + int(num2[0]) + int(num2[1])
        print(suma)


# 9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito. 
def funcion9():
    num= str(input("Digite un numero de 3 digitos: "))

    if(len(num)!=3):
        print("El numero debe contener 3 digitos.")
    else:
        maximo = str(max(int(num[0]), int(num[1]), int(num[2])))
        print(maximo)
        print(f"Posición del numero mas alto: {num.find(maximo)}")


# 10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros. 
def funcion10():
    num= str(input("Digite un numero de 3 digitos: "))
    arre= []

    if(len(num)!=3):
        print("El numero debe contener 3 digitos.")
    else:
        num2=int(len(num))
        print(num2)
        for a in range(0, num2):
            for b in range(0, num2):

                modu= int(num[b]) % int(num[a])
                print(f"{num[b]} % {num[a]}= {modu}")
                if modu==0:
                    arre.append(f"{num[b]} es multiplo de {num[a]}")
        print(arre)



# 11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito. 
def funcion11():
    print("Digite numeros en los inputs (max 2 digitos)")
    num1= str(input("Input 1: "))
    num2= str(input("Input 2: "))
    num3= str(input("Input 3: "))

    if(len(num1)!=2 or len(num2)!=2 or len(num3)!=2):
        print("Se deben digitar solo numeros con 2 digitos")
    else:
        maximo= str(max(int(num1[0]) ,int(num1[1]), int(num2[0]) , int(num2[1]), int(num3[0]) , int(num3[1])))

        if maximo in num1:
            print(f"El max.numero {maximo}, esta en el input 1")
        elif maximo in num2:
            print(f"el max.numero {maximo}, esta en el input 2")
        elif maximo in num3:
            print(f"el max.numero {maximo}, esta en el input 3")

# 12. Leer un número entero de suma de los otros dos. 
#????


# 13. Leer un número entero menor que 50 y positivo y determinar si es un número primo. 
def  funcion13():
    from math import factorial

    continuar=0
    while continuar==0:
        num= int(input("Digite un numero menor a 50: "))

        if num>50:
            print("El numero NO puede ser mayor a 50")
        elif num<0:
            print("El numero es negativo")
        else:
            formula=factorial((num-1)) +1

            if formula%num==0: 
                print("El numero es primo")
            else:
                print("El numero no es primo")

        #Bucle de continuacion
        preg= str(input("Contuniar? S/N: "))
        if preg=="S" or preg=="s":
            continuar=0
        else:
            continuar=1

# 14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
def funcion14():
    num= str(input("Digite un numero con 4 digitos: "))

    if len(num)!=4:
        print("El numero debe tener 4 digitos")
    else:
        if (num[1]==num[2]):
            print(f"Los digitos 2 y penultimo son iguales")
        else:
            print(f"Los digitos no son iguales")


# 15. Leer un número entero y determinar si es múltiplo de 7. 
def funcion15():
    num= int(input("Digite un numero: "))

    if num%7==0:
        print(f"El numero {num} es multiplo de 7")
    else:
        print(f"El numero {num} NO es multiplo de 7")



# 16. Leer un número entero menor que mil y determinar cuántos dígitos tiene. 
def funcion16():
    num= int(input("Digite un numero menor a 1000: "))

    if num>1000:
        print("debe digitar un numero menor a 1000")
    else:
        largo=len(str(num))
        print(f"El numero tiene {largo} digitos.")

# 17. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares. 
def funcion17():
    pares=0
    impar=0
    num= str(input("Digite un numero de 4 digitos: "))

    if len(num)!=4:
        print("El numero debe tener 4 digitos")
    else:
        for a in range(0,4):
            if int(num[a])%2==0:
                pares=pares+1
            else:
                impar=impar+1
        print(f"Cantidad pares: {pares}")
        print(f"Cantidad impares: {impar}")

# 18. Leer tres números enteros y determinar si el último dígito de los tres números es igual. 
def funcion18():
    num1= str(input("Digite un numero: "))
    num2= str(input("Digite otro numero: "))
    num3= str(input("Digite ultimo numero: "))

    a=int(num1[len(num1)-1])
    b=int(num2[len(num2)-1])
    c=int(num3[len(num3)-1])

    conjunto=set()
    contar=0
    conjunto.add(a)
    conjunto.add(b)
    conjunto.add(c)

    for con in conjunto:
        contar=contar+1

    if(contar==1):
        print("Los ultimos numeros son iguales")
    else:
        print("Los ultimos numeros NO SON IGUALES")



# 19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la 
# cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las 
# horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa 
# ingresadas por el usuario.
def funcion19():
    horas = int(input("Ingrese las horas trabajadas: "))
    tarifa= int(input("Ingrese la tarifa x hora: "))
    neto=0

    if horas<=40:
        salario= tarifa*horas
        extras=0
        neto=salario+extras
    else:
        salario= tarifa*40
        extras = tarifa*(horas-40) + (tarifa*(horas-40))*0.5
        neto   = salario+extras

    print("////////////////////////////////")
    print("Valor a pagar:")
    print(f"Valor salario basico: {salario}")
    print(f"Valor   horas extras: {extras}")
    print(f"Valor salario   Neto: {neto}")


# 20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran 
# tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son 
# menos de tres camisas un descuento del 10%
def funcion20():
    camisa  =int(input("Digite el valor de las camisas: "))
    cantidad=int(input("Cuntas unidades llevara?: "))

    total= (camisa*cantidad) 
    if cantidad<3:
        descuento="10%"
        valorDescuento=(camisa*cantidad)*0.1
        totalNeto= (camisa*cantidad) - valorDescuento
    else:
        descuento="20%"
        valorDescuento=(camisa*cantidad)*0.2
        totalNeto= (camisa*cantidad) -valorDescuento

    print("///////////////////////////////////////////////")
    print(f"Valor de las camisas: {total}")
    print(f"Valor descuento({descuento}): {valorDescuento}")
    print(f"Valor Final: {totalNeto}")


# 21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y 
# 5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó 
# o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro 
# del rango permitido.

def funcion21():
    nota1= float(input("Ingrese Nota 1: "))
    nota2= float(input("Ingrese Nota 2: "))
    nota3= float(input("Ingrese Nota 3: "))

    if nota1<0 and nota1>5 or nota2<0 and nota2>5 or nota3<0 and nota3>5:
        print("Las notas deben estar en un rango de 0 a 5")
    else:
        prom=(nota1+nota2+nota3)/3

    if(prom>3):
        print(f"Nota Final: {prom} - El estudiante aprobo")
    else:
        print(f"Nota Final: {prom} - El estudiante NO aprobo")


# 22. Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es 
# palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor 
# a roma”.
def funcion22():
    texto= str(input("Ingrese texto: "))
    invertida =texto[::-1]

    if texto==invertida:
        print("El texto es un palíndromo")
    else:
        print("El texto NO es un palíndromo")
    print(f"Invertido: {invertida}")


# 23. Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario 
# mediante input el valor del primer número, el valor del segundo número y la operación a 
# realizar, hay que tener en cuenta la validación de los valores de entrada, 
# por ejemplo:Si el programa pide el primer valor, y el usuario ingresa una letra, combinaciones de 
# números y letras o caracteres no numéricos se debe mostrar un mensaje mediante otro input 
# requiriendo que ingrese nuevamente el numero e indicándole al usuario que el carácter 
# ingresado debe ser numérico.
# En el caso que uno de los valores ingresados sea 0 y el usuario ingrese la opción de 
# División, debe imprimir un mensaje donde se indique que no se pude dividir entre cero o 
# que el cero no puede ser dividido.

def funcion23():
    continuar=0
    while continuar==0:
        print("////////////////////////////////////////////////////////")
        valor1= str(input("Ingrese valor 1: "))
        valor2= str(input("Ingrese valor 2: "))

        op = str(input("Ingrese tipo operacion(sum-res-div-mul): "))

        if valor1.isdigit() and valor2.isdigit():

            if(op=="sum"):
                final=int(valor1)+int(valor2)
                print(f"{valor1}+{valor2}={final}")
                continuar=1

            elif(op=="res"):
                final=int(valor1)-int(valor2)
                print(f"{valor1}-{valor2}={final}")
                continuar=1

            elif(op=="mul"):
                final=int(valor1)*int(valor2)
                print(f"{valor1}*{valor2}={final}")
                continuar=1
            
            elif(op=="div"):
                if int(valor2)==0:
                    print("No se puede hacer una division por cero (0).")
                else:
                    final=int(valor1)/int(valor2)
                    print(f"{valor1}/{valor2}={final}")
                    continuar=1

            else:
                print("En tipo de operacion solo puede digitar alguna de estas 4 opciones, (sum-res-div-mul).")
        else:
            print("Debe ingresar en valor 1 y valor 2 SOLO NUMEROS.")






