#Metodo que realiza busqueda binaria en un arreglo ordenado
def busqueda_Binaria(arreglo, target, izq, der):
    while izq <= der:
        mitad = (izq + der) // 2
        if arreglo[mitad] == target:
            return mitad
        elif arreglo[mitad] < target:
            izq = mitad + 1
        else:
            der = mitad - 1
            #Si no se encuentra el target, retornamos -1
    return -1

#EJercicio 1: Dado un arreglo y un target, devuelve true si existen dos numeros en el arreglo que sumados den el target y 
#los muestra en terminal. En caso contrario, devuelve false y muestra en terminal [-1, -1].
#Complejidad: O(n log n)
def encontrar_suma(arr, target):
    arr.sort()
    for s_i in range(len(arr)):
        conmplemento = target - arr[s_i]
        s_j = busqueda_Binaria(arr, conmplemento, 0, len(arr) - 1)
        if s_j != -1 and s_j != s_i:
            print("Existen dos números en el arreglo donde la suma de ambos es igual a target.")
            arr_suma = [arr[s_i], arr[s_j]]
            print(f"Los números son: ")
            for elem in arr_suma:
                print(elem)
            return True  
        
    print("NO existen dos números en el arreglo donde la suma de ambos es igual a target.")
    arr1 = [-1, -1]
    for elem in arr1:
        print(elem)
    return False  # Retornamos False si no se encuentran sumandos que den el target

# Ejemplo
arr = [2, 6, 1, 9, 4]
target = 15
resultado = encontrar_suma(arr, target)


#Ejercicio 2: Implementación de un árbol binario ordenado utilizando la palabra reservada
#class. El árbol cumple con poder ejecutar los 3 recorridos (preorden, inOrden y PostOrden).
#Se incluye el metodo agregar. 

#Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato      #Dato que se guarda en el nodo
        self.izquierda = None #Hijo izquierdo
        self.derecha = None   #Hijo derecho

#Clase Arbol
class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)
        
    #Agregamos de forma recursiva un nuevo nodo al arbol Binario. Si es menor que el nodo actual,
    #se coloca a la izquierda, si es mayor, a la derecha.
    #Metodo privado
    def __agregar_aux(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_aux(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_aux(nodo.derecha, dato)
            
    #Metodo que recorre el arbol en InOrden.
    #Visita el subArbol izquierdo, luego la raiz y luego el subArbol derecho.
    def __inOrden_aux(self, nodo):
        if nodo is not None:
            self.__inOrden_aux(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inOrden_aux(nodo.derecha)
        
    #Metodo que recorre el arbol en PreOrden.
    #Visita la raiz, recorre el subArbol izquierdo y luego el derecho.
    def __inPreOrden_aux(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__inPreOrden_aux(nodo.izquierda)
            self.__inPreOrden_aux(nodo.derecha)

    #Metodo que recorre el arbol en PostOrden.
    #Visita el subArbol izquierdo, luego el derecho y luego la raiz.
    def __postOrden_aux(self, nodo):
        if nodo is not None:
            self.__postOrden_aux(nodo.izquierda)
            self.__postOrden_aux(nodo.derecha)
            print(nodo.dato, end=", ")

    def agregar(self, dato):
        self.__agregar_aux(self.raiz, dato)

    def inOrden(self):
        print("Recorrido InOrden: ")
        self.__inOrden_aux(self.raiz)
        print("")

    def inPreOrden(self):
        print("Recorrido PreOrden: ")
        self.__inPreOrden_aux(self.raiz)
        print("")
    
    def postOrden(self):
        print("Recorrido PostOrden: ")
        self.__postOrden_aux(self.raiz)
        print("")
        
#Ejemplo
arbol = Arbol(10)  #Nodo raiz
arbol.agregar(8)
arbol.agregar(12)
arbol.agregar(6)
arbol.agregar(9)
arbol.agregar(11)
arbol.agregar(13)

arbol.inOrden()
arbol.inPreOrden()
arbol.postOrden()