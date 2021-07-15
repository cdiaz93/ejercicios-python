#Leer el material de conjuntos unidad 3 y hacer ejemplos sencillos de las funciones para conjuntos
#Hacerlos basandose en el material desde la funcion isdisjoint() hasta update().



#isdisjoint() 
# devuelve el valor True si no hay elementos comunes entre los conjuntos mutables o  inmutables.
def funcion1()->set[int]:
    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    set_mutable1.isdisjoint(set_mutable2)
    return set_mutable1


#issubset()
# devuelve el valor True si el conjunto mutable es un subconjunto del conjunto mutable o del conjunto inmutable argumento.
def funcion2():
    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    set_mutable3 = set([11, 5, 2, 4])
    print(set_mutable2.issubset(set_mutable1))
    print(set_mutable3.issubset(set_mutable1))


#issuperset()
#devuelve el valor True si el conjunto mutable o el conjunto inmutable es un superset del conjunto mutable argumento.
def funcion3():
    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    set_mutable3 = set([11, 5, 2, 4])
    print(set_mutable1.issuperset(set_mutable2))
    print(set_mutable1.issuperset(set_mutable3))


#pop()
#Remueve arbitrariamente y devuelve un elemento de conjunto mutable. 
#El método pop() no toma ningún argumento. 
# Si el conjunto mutable esta vacío se lanza una excepción KeyError.
def funcion4():
    paquetes = {'python', 'zope', 'plone', 'django'}
    print("Valor aleatorio devuelto es:", paquetes.pop())


#remove()
#busca y remueve un elemento de un conjunto mutable
def funcion5():
    paquetes = {'python', 'zope', 'plone', 'django'}
    paquetes.remove('django')


#symmetric_difference()
#devuelve todos los elementos que están en un conjunto mutable e conjunto inmutable u otro, pero no en ambos.
def funcion6():
    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    print(set_mutable1.symmetric_difference(set_mutable2))


#symmetric_difference_update()
#actualiza un conjunto mutable llamando al método symmetric_difference_update() con los conjuntos de diferencia simétrica.
#La diferencia simétrica de dos conjuntos es el conjunto de elementos que están en cualquiera de los conjuntos pero no en ambos
def funcion7():
    proyecto1 = {'python', 'plone', 'django'}
    proyecto2 = {'django', 'zope', 'pyramid'}
    proyecto1.symmetric_difference_update(proyecto2)


#union()
#devuelve un conjunto mutable y conjunto inmutable con todos los elementos que están en alguno de los conjuntos mutables y conjuntos inmutables.
def funcion8():
    set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    set_mutable2 = set([11, 5, 9, 2, 4, 8])
    print(set_mutable1.union(set_mutable2))


#update()
#agrega elementos desde un conjunto mutable (pasando como un argumento) 
# un tipo tupla, un tipo lista, un tipo diccionario o un tipo conjunto mutable llamado con el método update().
def funcion8():
    version_plone_dev = set(["gato", "perro"])
    versiones_plone = set(["buho", "gallina", "cacatua", "caballo"])
    print(version_plone_dev)
    print(versiones_plone)

    versiones_plone.update(version_plone_dev)
    print(versiones_plone)

def funcion9():
    a=set()
    a={1,2,3,4,5,6,7}
    print(4 in a)
    print(8 not in a)
    print(len(a))


def funcion10():
    gruposCalificados ={'P45','P61','P33','P87'}

    #Observar el tipo que ha sifo identificado
    print("Grupos calificados es de tipo:",type(gruposCalificados))
    gruposCalificados.add('P17')
    gruposCalificados.add('P17')
    gruposCalificados.remove('P45')

    print(gruposCalificados)

    if 'P17' in gruposCalificados:
        print('P17 ya ha sido calificado!')



#--------------------------------------------------------------
funcion10()
