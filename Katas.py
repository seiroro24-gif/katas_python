

#Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def Ejercicio1():
    #Pedimos al usuario que introduzca la cadena de texto
    cadena_de_texto =  input("Introduce una cadena de texto: ")
    #Convertimos la cadena de texto una tupla para que luego sus caracteres puedan ser contados con la funcion .count
    cadena = tuple(cadena_de_texto)
    print ("Aqui tiene sus caracteres con su frecuencia correspondiente: ")
    #Creamos un bucle for para que se repita la funcion .count
    for letra in cadena:
        #Creamos el condicional if para excluir al espacio de nuestro conteo
        if letra != " ":
            #Creamos el diccionario
            diccionario = {}
            #Asignamos a cada letra su correspondiente frecuencia
            diccionario [letra] = cadena.count(letra)
            print (diccionario)




# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
def Ejercicio2():
    #Creamos la lista
    lista = []
    #Usamos el bucle while para crear en esencia eso, un bucle, asi se pueden añadir los daots de la lista
    while True:
    
        numero = input("Introduce los numeros y escriba fin para acabar: ")
        #Para que acabe el input de valores tomamos el valor fin y lo convertimos a minusculas para aceptar cualquier variacion de fin del usuario
        if numero.lower() == "fin":
            break
        #Añadimos los valores a la lista con la funcion append y los convertimos en int ya que se reciben como string
        lista.append(int(numero)) 

    #Creamos la función que duplica un número
    def duplicar(doble):
        return doble * 2

    #Aplicamos map para duplicar los valores de la lista
    print(list(map(duplicar, lista)))



#Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def Ejercicio3():
    #Creamos la lista y la lista de palabras clave (resultado)
    resultado =[]
    lista = []
    #Usamos el bucle while para crear en esencia eso, un bucle, asi se pueden añadir los daots de la lista
    while True:
       
           palabra_introducida = input("Introduce las palabras y escriba fin para acabar: ")
           #Para que acabe el input de valores tomamos el valor fin y lo convertimos a minusculas para aceptar cualquier variacion de fin del usuario
           if palabra_introducida.lower() == "fin":
               break
           #Añadimos los valores a la lista con la funcion append y los convertimos en int ya que se reciben como string
           lista.append(palabra_introducida) 
    parametro = input ("Introduzca la palabra clave: ")
    #Creamos un bucle for con un condicional if que nos permitan buscar las palabras que sigan el parametro en la lista
    for palabra in lista :
         if parametro in palabra:
              #Creamos una nueva lista que contenga las palabras calves 
              resultado.append(palabra)
    print (resultado)    



#Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
def Ejercicio4 ():
   #Creamos ambas listas
   lista1 = []
   lista2 = []
   #Creamos una funcion que nos permita crear listas 
   def introducir_numeros ():
      lista = []
      while True:
              numero = input("Introduce los numeros y escriba fin para acabar: ")
              #Para que acabe el input de valores tomamos el valor fin y lo convertimos a minusculas para aceptar cualquier variacion de fin del usuario
              if numero.lower() == "fin":
                  break
              #Añadimos los valores a la lista con la funcion append y los convertimos en int ya que se reciben como string
              lista.append(int (numero))
      return lista
  
   lista1 = introducir_numeros ()
   lista2 = introducir_numeros ()
   print ("La diferencia de las listas son: ")
   #Creamos una segunda funcion que nos permita calcualr la diferencia de estas dos listas para lurgo usarla con map()
   def diferencia(a,b):
        return a - b
   print (list(map(diferencia,lista1,lista2)))


#Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def Ejercicio5 ():
    #Declaramos las variables que se usaran a lo largo del codigo
    lista = []
    nota_aprobado = 5.0
    nota_total = 0 
    numero_notas = 0
    nota_final = ""
     #Usamos el bucle while para crear en esencia eso, un bucle, asi se pueden añadir los datos en la lista
    while True:
        numero = input("Introduce los numeros (0-10) y escriba fin para acabar: ")
        #Para que acabe el input de valores tomamos el valor fin y lo convertimos a minusculas para aceptar cualquier variacion de fin del usuario
        if numero.lower() == "fin":
            break
        #Pasamos de string a numero para que pueda ser comparado con otros nuemros 
        numero = int (numero)  
        #creamos un condicional que nos permita saber si el numero se encunetra dentro de los parametros
        if numero >= 0 and numero <= 10:
                #Añadimos los numeros a la lista
                lista.append(numero)
        else:
            print ("Numero fuera de rango")
    #Funcion for que nos permite contar el numero total de notas en la lista
    for nota in lista:
        numero_notas += 1
    #Funcion for que nos pemite sacar los numeros de la lista y sumarlos
    for nota in lista:
        nota_total += nota 
    #Se calcula la media con la suma total de notas entre el numero de notas
    media = nota_total / numero_notas
    print ("La media es: ",media)
    #Funcion if para identificar cuando la media es aprobado o suspenso
    if media >= nota_aprobado:
         nota_final = "Aprobado"
    else :
         nota_final = "Suspenso"
    #Creamos la tupla solicitada
    tupla = (media,nota_final) 
    print(tupla)    


#Escribe una función que calcule el factorial de un número de manera recursiva.
def Ejercicio6 ():
    #Definimos la funcion factorial que multilica un numero por el la  funcion factorial del mismo numero asi hasta llegar a uno
    def factorial (x):
        if x == 1:
            return 1
        else:
            return x * factorial(x-1)
    numero = int(input("Escribe el nuemero"))
    print (factorial(numero))


#Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
def Ejercicio7 ():
    #Creamos la lista de tuplas
    lista_tuplas = [(1,2),(3,4),(4,5),(6,7)]
    #Creamos una funcion que nos permita cambiar esa tupla por una cadena de caracteres string
    def cambio_lista (tupla):
        lista_string = []
        string = str(tupla)
        return string
    #COnvertimos el resultado de la funcion map a una lista
    print (list(map(cambio_lista,lista_tuplas)))



#Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
def Ejercicio8 ():
    #Pedimos los numeros
    numero1 = input ("Introduzca el primer numero")
    numero2 = input ("Introduzca el segundo numero")
    #Usamos la funcion try para que si nos da ValueError al tratar de convertir el string introucido a float apaprezca que se debe introducir un valor numerico
    try:
       numero1 = float(numero1)
       numero2 = float(numero2)
       #Usamos la funcion if para descartar el valor 0 en el segundo numero y asi no dividir entre 0
       if numero2 == 0:
            print ("No es posible dividir entre cero" )
       else:
            print ("El resultado de la division es: \n", numero1 / numero2)
    except ValueError:
        print ("No ha introducido un numero, porfavor vuelva a intentar")


#Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
def Ejercicio9 ():
    #Establecemos una lista con todos los animales y otra con todos los animales prohibidos
    lista = ["Perro","Gato","Conejo","Canario","Tortuga","Hamster","Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    #definimos una funcion que nos compare las dos listas y nos devuelva en una lista usando la funcion filter las mascotas no prohibidas
    def mascotas_prohibidas (mascota):
        return mascota not in prohibidas
    print(list(filter(mascotas_prohibidas,lista)))


#Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
def Ejercicio10():
    #Creamos la lista y las variables que usaremos para calcular el promedio
    numero_valores = 0
    suma = 0
    lista = []

    #Usamos el bucle while para poder introducir varios numeros hasta que el usuario escriba fin
    while True:

        palabra_introducida = input("Introduce los numeros y escriba fin para acabar: ")

        #Usamos try para controlar los errores si el usuario introduce un valor que no sea un numero
        try:
            #Si el usuario escribe fin terminamos el bucle
            if palabra_introducida.lower() == "fin":
                break

            #Añadimos los numeros a la lista convirtiendolos previamente a enteros con int
            lista.append(int(palabra_introducida))

            #Sumamos uno a la variable numero_valores para saber cuantos numeros hay en la lista
            numero_valores += 1

        #Si el usuario introduce un valor no valido mostramos un mensaje de error
        except ValueError:
            print("Introduce un valor valido")

    #Creamos una clase para declarar una excepcion personalizada para listas vacias
    class ErrorVacio(Exception):
        pass

    try:
        #Comprobamos si la lista esta vacia y si es asi, lanzamos la excepcion personalizada 
        if not lista:
            raise ErrorVacio

        #Recorremos la lista y sumamos todos sus valores
        for valor in lista:
            suma += valor

        #Calculamos y mostramos el promedio de los numeros introducidos
        print("El promedio total:", float(suma / numero_valores))

    #Si la lista esta vacia mostramos un mensaje de error
    except ErrorVacio:
        print("La lista esta vacia")


#Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def Ejercicio11():
    edad = input ("Introduzca su edad:")
    try: 
        #Comprobamos si el string introducido se puede convertir a numero
        edad = int (edad)
        #Establecemos el rango de edad
        if edad < 0 or edad > 120:
            print("Su edad se encuentra fuera del rango")
        else :
            print ("Se ha introducido su edad correctamente")
    except ValueError:
        #Si el string introducido no es un numero salta el error
        print ("Porfavor, introduzca un valor valido")


#Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
def Ejercicio12():
    #Solicitamos la frase
    frase = input("Introduce la frase:")
    #Guarda las palabras de la frase en una lista
    lista_palabras = frase.split()
    #Creamos una función que devuelve la longitud de una palabra
    def contar_palabras(palabra):
        return len(palabra)
    #Imprimios la lista de palabras
    print(lista_palabras)
    #Aplicamos la función a cada palabra mediante map 
    print(list(map(contar_palabras, lista_palabras)))


#Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def Ejercicio13():
    #Solicitamos el conjunto de letras
    conjunto = input("Introduzca el conjunto de letras:")
    #Comprobamos que todos los caracteres sean letras
    if not conjunto.isalpha():
        print("No todo son letras, por favor vuelva a intentarlo")
    else:
        #Convertimos todas las letras a minúsculas
        conjunto = conjunto.lower()
        #Eliminamos las letras repetidas
        quitar_duplicados = set(conjunto)
        #Creamos una función que devuelve una tupla con la letra en mayúscula y minúscula
        def conversor(letra):
            letra_mayuscula = letra.upper()
            letra_minuscula = letra.lower()
            return (letra_mayuscula, letra_minuscula)
        #Aplicamos la función a cada letra mediante map e imprimimos el resultado
        print(list(map(conversor, quitar_duplicados)))


#Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
def Ejercicio14():
    #Creamos una lista vacía donde guardamos las palabras
    lista = []
    #Solicitamos palabras hasta que el usuario escriba fin
    while True:
        palabra = input("Introduce las palabras de la lista de una en una y escribe fin para acabar")
        if palabra.lower() == "fin":
            break
        lista.append(palabra)
    #Solicitamos la letra por la que deben empezar las palabras
    letra = input("Introduzca la letra en especifico: ")
    #Creamos una función que comprueba si una palabra empieza por la letra indicada
    def empieza_letra(palabra):
        return palabra.startswith(letra)
    #Aplicamos la función a cada palabra mediante filter e imprimimos el resultado
    print(list(filter(empieza_letra, lista)))


#Crea una función lambda que sume 3 a cada número de una lista dada.
def Ejercicio15():
    #Creamos una lista vacía donde guardaremos los números
    lista = []
    #Solicitamos números hasta que el usuario escriba fin
    while True:
        numero = input("Introduzca los numeros y acaba con un fin")
        if numero == "fin":
            break
        lista.append(int(numero))
    #Aplicamos la función lambda a cada número mediante map e imprimimos el resultado
    print(list(map(lambda numero: numero + 3, lista)))


#Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
def Ejercicio16():
    #Creamos una lista vacía donde guardamos las palabras
        frase = input("Inrtroduzca la cadena de texto; ")
        lista = frase.split()
        #Solicitamos el numero de la lonquitud de las palabras
        while True:
            numero = int(input("Introduzca el numero de la lonquitud de las palabras: "))

            if numero > 0  and numero <15:
                  break
            else:
                  print ("Es ciomplicado que una palabra tenga esa cantidad de letras, porfavor prueb otra vez.")
                  continue
        #Creamos una función que comprueba si la longuitud de la palabra es del numero establecido
        def longuitud_palabra(palabra):
              if len(palabra) >= numero:
                    return palabra
        print (list(filter(longuitud_palabra,lista)))


#Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
from functools import reduce
def Ejercicio17():
      #Creamos una lista vacía donde guardaremos los números
        lista = []
        #Solicitamos números hasta que el usuario escriba fin
        while True:
            numero = input("Introduzca los numeros y acaba con un fin")
            if numero == "fin":
                break
            lista.append(numero)
        print(reduce(lambda a,b:a + b,lista))


#Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
def Ejercicio18():
    #Creamos una lista de diccionarios con la información de los estudiantes
    lista =[{"nombre":"Juan","edad":18,"calificacion":90},{"nombre":"David","edad":18,"calificacion":50},{"nombre":"Maria","edad":19,"calificacion":100},{"nombre":"Juan","edad":20,"calificacion":30}]
    #Creamos una función que comprueba si la calificación es mayor o igual a 90
    def estudiantes_aprobados(diccionario):
        calificacion = diccionario.get("calificacion")
        return calificacion >= 90
    #Aplicamos filter para obtener los estudiantes aprobados e imprimimos el resultado
    print(list(filter(estudiantes_aprobados,lista)))


#Crea una función lambda que filtre los números impares de una lista dada.
def Ejercicio19():
    #Creamos una lista con números del 1 al 15
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #Mostramos la lista original
    print("La lista es: ",lista)
    #Aplicamos filter para obtener únicamente los números impares e imprimimos el resultado
    print("La lista de numeros impares es: ",list(filter(lambda numero: numero % 2 != 0,lista)))


#Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
def Ejercicio20():
    #Creamos una lista con números y cadenas de texto
    lista = [1,2,3,"Hola","4",5,6,"gato","7","8",9]
    #Aplicamos filter para obtener únicamente los valores de tipo int e imprimimos el resultado
    print(list(filter(lambda elemento: isinstance(elemento,int),lista)))


#Crea una función que calcule el cubo de un número dado mediante una función lambda.
def Ejercicio21():
    #Solicitamos un número hasta que el usuario introduzca un valor válido
    while True:
        numero = input("Introduzca un numero: ")
        try:
            numero = int(numero)
            break
        except ValueError:
            continue
    #Creamos una función lambda que calcula el cubo de un número
    funcion = lambda numero: numero ** 3
    #Calculamos el cubo e imprimimos el resultado
    print(funcion(numero))


#Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
from functools import reduce
def Ejercicio22():
    #Creamos una lista vacía donde guardaremos los números
    lista = []
    #Solicitamos números hasta que el usuario escriba fin
    while True:
        numero = input("Introduzca los valores de la lista y escriba fin para finalizar: ")
        try:
            numero = int(numero)
            lista.append(numero)
            continue
        except ValueError:
            if numero.lower() == "fin":
                break
            else:
                continue
    #Calculamos el producto de todos los valores mediante reduce
    print(reduce(lambda a,b: a*b,lista))


#Concatena una lista de palabras. Usa la función reduce().
def Ejercicio23():
    #Creamos una lista vacía donde guardaremos las palabras
    lista = []
    #Solicitamos palabras hasta que el usuario escriba fin
    while True:
        palabra = input("Introduzca las palabras y escriba fin para acabar: ")
        if palabra.lower() == "fin":
            break
        lista.append(palabra)
    #Concatenamos todas las palabras mediante reduce
    print(reduce(lambda a,b: a + " " + b,lista))


#Calcula la diferencia total en los valores de una lista. Usa la función reduce().
from functools import reduce
def Ejercicio24():
    #Creamos una lista vacía donde guardaremos los números
    lista = []
    #Solicitamos números hasta que el usuario escriba fin
    while True:
        numero = input("Introduzca los numeros y escriba fin para finalizar: ")
        try:
            numero = int(numero)
            lista.append(numero)
            continue
        except ValueError:
            if numero.lower() == "fin":
                break
            else:
                continue
    #Calculamos la diferencia total de los valores mediante reduce
    print(reduce(lambda a,b: a - b, lista))


#Crea una función que cuente el número de caracteres en una cadena de texto dada
def Ejercicio25():
    #Solicitamos una cadena de texto al usuario
    cadena = input("Introduzca la cadena de texto: ")
    #Calculamos el número de caracteres de la cadena e imprimimos el resultado
    print(len(cadena))


#Crea una función lambda que calcule el resto de la división entre dos números dados.
def Ejercicio26():
    #Solicitamos los dos números
    numero1=int(input("Introduzca el primer numero: "))
    numero2=int(input("Introduzca el segundo numero: "))
    #Creamos la función lambda que calcula el resto
    funcion=lambda numero1,numero2:numero1%numero2
    #Mostramos el resultado
    print(funcion(numero1,numero2))


#Crea una función que calcule el promedio de una lista de números.
def Ejercicio27():
    #Creamos las variables necesarias
    lista=[]
    longitud=0
    numero_total=0
    #Solicitamos números hasta que el usuario escriba fin
    while True:
        numero=input("Introduzca los numeros y escriba fin para finalizar: ")
        try:
            numero=int(numero)
            lista.append(numero)
            continue
        except ValueError:
            if numero.lower()=="fin":
                break
            else:
                continue
    #Calculamos la longitud de la lista y la suma de sus elementos
    for numero in lista:
        longitud+=1
        numero_total+=numero
    #Mostramos el promedio
    print(numero_total/longitud)


#Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def Ejercicio28():
    #Lista donde se guardan los elementos introducidos
    lista = []
    #Variable que controla la salida del programa
    elemento = ""
    #Comprueba si un elemento ya está en la lista
    def duplicado(elemento):
        for valores in lista:
            if valores == elemento:
                return elemento
    #Pide elementos hasta que se escriba "fin"
    while elemento.lower() != "fin":
        #Solicita un elemento al usuario
        elemento = input("Introduce un numero y escriba fin para salir: ")
        #Muestra el elemento si está duplicado
        print(duplicado(elemento))
        #Añade el elemento a la lista
        lista.append(elemento)


#Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
def Ejercicio29():
    #Solicita la variable al usuario
    variable = input("Introduzzca su variable")
    #Convierte la variable en una lista de caracteres
    lista = list(variable)
    #Sustituye por '#' todos los caracteres excepto los últimos cuatro
    for i in range(0, len(lista)-4):
        lista[i] = "#"
    #Muestra el resultado
    print(lista)


#Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def Ejercicio30():
    #Solicita las dos palabras y las convierte a minúsculas
    lista1 = list(input("Introduzca la primera palabra: ").lower())
    lista2 = list(input("Introduzca la segunda palabra: ").lower())
    #Comprueba si las palabras tienen las mismas letras
    if sorted(lista1) == sorted(lista2):
        print("Las palabras son anagramas")
    else:
        print("Las palabras no son anagramas")


#Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
def Ejercicio31():
    lista = []
    # Pedimos nombres hasta que el usuario escriba "fin".
    while True:
        nombre = input("Introduzca un nombre y escriba fin para finalizar: ")
        if nombre.lower() == "fin":
            break
        lista.append(nombre)

    # Comprobamos si el nombre a buscar está en la lista.
    nombre_comparacion = input("Introduzca un nombre para buscarlo en la lista: ")
    if nombre_comparacion in lista:
        print("Su nombre aparece en la lista.")
    else:
        raise ValueError("El nombre especificado no se encuentra en la lista.")



#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def Ejercicio32():
    empleados = [
    "juan", "Programador",
    "ana", "Diseñadora",
    "luis", "Gerente",
    "marta", "Contable",
    "pedro", "Marketing",
]

    # Pedimos el nombre del empleado.
    nombre = (input("Escriba el nombre de la persona: ")).lower()

    # Si el nombre existe en la lista, mostramos su profesión.
    if nombre in empleados:
        print(f"La profesion de {nombre} es: {empleados[empleados.index(nombre)+1]}")
    else:
        # Si no existe informamos.
        print("La persona introducida no trabaja aqui.")



#Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def Ejercicio33():
    lista1 = [1,2,3,4,5,6,7,8,9,0]
    lista2 = [0,9,8,7,6,5,4,3,2,1]

    # map recorre ambas listas a la vez y aplica la lambda a cada par de elementos.
    print(list(map(lambda a,b: a + b, lista1, lista2)))


# Crea la clase Arbol
#  Define un árbol genérico con un tronco y ramas como atributos.
#     Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
#     Código a seguir:
#         Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#         Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#         Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#         Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#         Implementar el método quitar_rama para eliminar una rama en una posición específica.
#         Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
#     Caso de uso: a. Crear un árbol. b. Hacer crecer el tronco una unidad. c. Añadir una nueva rama. d. Hacer crecer todas las ramas una unidad. e. Añadir dos nuevas ramas. f. Retirar la rama situada en la posición 2. g. Obtener información sobre el árbol.
def Ejercicio34():
    class Arbol:
        # Inicializa el tronco y las ramas.
        def __init__(self,tronco,ramas):
            self.tronco = tronco
            self.ramas = ramas
        # Aumenta la longitud del tronco.
        def crecer_tronco(self):
            self.tronco += 1
        # Añade nuevas ramas.
        def nueva_rama(self,numero):
            for i in range(0,numero,1):
                self.ramas.append(1)
        # Hace crecer todas las ramas.
        def crecer_ramas(self):
            i = 0
            for rama in self.ramas:
                self.ramas[i] = rama + 1
                i += 1
        # Elimina una rama de la posición indicada.
        def quitar_ramas(self,posicion):
            self.ramas.pop(posicion - 1)
        # Muestra la información del árbol.
        def info_arbol(self):
            print(f"La longitud del tronco es {self.tronco}\nEl numero de ramas es {len(self.ramas)}")
            for i in range(0,len(self.ramas),1):
                print(f"La rama {i + 1} tiene una longitud de {self.ramas[i]}.")
    arbol = Arbol(1,[])
    arbol.crecer_tronco()
    arbol.nueva_rama(1)
    arbol.crecer_ramas()
    arbol.nueva_rama(2)
    arbol.quitar_ramas(2)
    arbol.info_arbol()

# Crea la clase UsuarioBanco
#     Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
#     Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
#     Código a seguir:
#         Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
#         Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
#         Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
#         Implementar agregar_dinero para aumentar el saldo del usuario.
#     Caso de uso: a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. b. Agregar 20 unidades al saldo de Bob. c. Transferir 80 unidades de Bob a Alicia. d. Retirar 50 unidades del saldo de Alicia.
def Ejercicio35():
    class UsuarioBanco:
        # Inicializa los datos del usuario.
        def __init__(self,nombre,saldo,cuenta_corriente):
            self.nombre = nombre
            self.saldo = saldo
            self.cuenta_corriente = cuenta_corriente
        # Retira dinero si hay saldo suficiente.
        def retirar_dinero(self,retirar_dinero):
            if retirar_dinero <= self.saldo:
                self.saldo -= retirar_dinero
            else:
                raise ValueError("Saldo insuficiente")
        # Transfiere dinero a otro usuario.
        def transferir_dinero(self,dinero,destinatario):
            if dinero <= self.saldo:
                self.saldo -= dinero
                destinatario.agregar_dinero(dinero)
            else:
                raise ValueError("Saldo insuficiente")
        # Añade dinero al saldo.
        def agregar_dinero(self,dinero):
            self.saldo += dinero
    Alicia = UsuarioBanco("Alicia",100,True)
    Bob = UsuarioBanco("Bob",50,True)
    Bob.agregar_dinero(20)
    Bob.transferir_dinero(80,Alicia)
    Alicia.retirar_dinero(50)


# Crea una función llamada procesar_texto
#
#     Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
#     Código a seguir:
#         Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
#         Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
#         Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
#         Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
#     Caso de uso:
#         Verificar el funcionamiento completo de procesar_texto.
def Ejercicio36():
    class procesar_texto:
        # Inicializa el objeto con el texto introducido.
        def __init__(self,texto):
            self.texto = texto
        # Cuenta las veces que aparece cada palabra.
        def contar_palabras(self):
            lista = self.texto.split()
            diccionario ={}
            for palabra in lista:
                diccionario[palabra] = lista.count(palabra)
            print(f"El conteo de palabras es: \n{diccionario}\n")
        # Reemplaza una palabra por otra.
        def reemplazar_palabras(self,palabra_original,palabra_aremplazar):
            print(f"{self.texto.replace(palabra_original,palabra_aremplazar)}\n")
        # Elimina una palabra del texto.
        def elimiar_palabra(self,palabra):
            print(f"{self.texto.replace(palabra,'')}\n")
        # Ejecuta la opción seleccionada por el usuario.
        def procesar_texto(self,opcion):
            if opcion.lower() == "contar":
                procesar.contar_palabras()
            elif opcion.lower() == "reemplazar":
                print("Introduzca la palabra que desea remplazar del texto: ")
                palabra_original = input("Introduzca la palabra que desea remplazar del texto: ")
                print("Introduce la palabra nueva que desa reemplazar: ")
                palabra_areemplazar = input("Introduce la palabra nueva que desa reemplazar: ")
                procesar.reemplazar_palabras(palabra_original,palabra_areemplazar)
            elif opcion.lower() == "eliminar":
                print("Escriba la palabra que desea eliminar")
                palabra = (input("Escriba la palabra que desea eliminar")).lower()
                procesar.elimiar_palabra(palabra)
            else:
                print("Opcion no valida, porfavor vuelva a intentar")
    texto = input("Introduzca el texto")
    procesar = procesar_texto(texto)
    while True:
        print("Eliga una opcion:")
        print("- Contar\n- Reemplazar\n- Eliminar\n- Salir\n")
        opcion = input()
        if opcion.lower() == "salir":
            break
        else:
            procesar.procesar_texto(opcion)


# Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
def Ejercicio37():
    hora = int(input("Introduzca la hora: "))
    if hora >= 0 and hora < 6:
        print("Es de noche.")
    elif hora >= 6 and hora < 12:
        print("Es de día.")
    elif hora >= 12 and hora < 20:
        print("Es de tarde.")
    elif hora >= 20 and hora <= 23:
        print("Es de noche.")
    else:
        print("La hora introducida no es válida.")


# Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
#
#     Reglas: 0 - 69: insuficiente 70 - 79: bien 80 - 89: muy bien 90 - 100: excelente
def Ejercicio38():
    # Pedimos la calificación del alumno.
    nota = int(input("Introduzca su calificacion: "))
    # Comprobamos en qué rango se encuentra la nota.
    if nota >= 0 and nota <= 69:
        print("Insuficiente")
    elif nota >= 70 and nota <= 79:
        print("Bien")
    elif nota >= 80 and nota <= 89:
        print("Muy bien")
    elif nota >= 90 and nota <= 100:
        print("Excelente")
    else:
        # Mostramos un mensaje si la nota no es válida.
        print("La nota introducida no es válida.")


#Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
def Ejercicio39():
    # Muestra las figuras disponibles
    print("\nElija entre:\n- Rectangulo\n- Circulo\n- Triangulo")
    # Solicita la figura al usuario
    figura = input("Escriba la figura de la cual desea clacular su area:")
    # Si la figura es un rectángulo o un triángulo
    if figura.lower() in ("rectangulo", "triangulo"):
        # Guarda altura y base en una tupla
        tupla = (int(input("Escriba la altura: ")), int(input("Escriba la base: ")))
        # Calcula el área del triángulo
        if figura.lower() == "triangulo":
            print(f"El area del triangulo es: {(tupla[0] * tupla[1]) / 2}")
        # Calcula el área del rectángulo
        else:
            print(f"El area del rectangulo es: {tupla[0] * tupla[1]}")
    # Si la figura es un círculo
    elif figura.lower() == "circulo":
        # Guarda el radio en una tupla de un único elemento
        tupla = (int(input("Introduce el radio de la circunferencia: ")),)
        # Calcula el área del círculo
        print(f"El area del circulo es: {3.14 * tupla[0] * tupla[0]}")
    # Si la figura introducida no es válida
    else:
        print("Se ha introdducido una opcion no valida")
# Llama a la función


# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
def Ejercicio40():
    # Solicita el precio original del producto
    precio = int(input("Introduzca el precio origina del producto: "))
    while True:
        # Pregunta si el usuario tiene cupón
        cupon = input("¿Tienes cupon de descuento?")
        # Inicializa el precio final con el precio original
        precio_final = precio
        # Si tiene cupón
        if cupon.lower() == "si":
            # Solicita el porcentaje de descuento
            valor_cupon = int(input("Introduzca el porcentaje del cupon"))
            # Comprueba que el porcentaje sea válido
            if valor_cupon > 0:
                # Calcula el descuento aplicado al precio
                precio_final = precio -(valor_cupon / 100 * precio)
                break
            else:
                # Muestra un mensaje si el cupón no es válido
                print("Cupon de descuento no valido")
                break
        # Si no tiene cupón
        elif cupon.lower() == "no":
            break
        # Si la respuesta no es válida
        else:
            print("Respuesta no valida, porfavor intentelo de nuevo")
            continue
    # Muestra el precio final
    print(f"El precio total del producto es {precio_final}")
# Ejecuta la función

# Creamos un bucle para que el usuario pueda ejecutar todos ejercicios
while True:

    # Solicitamos al usuario el número del ejercicio que desea ejecutar
    ejercicio = input("Escriba el número del ejercicio que desea ejecutar (1-40) y escriba fin para salir: ")

    # Si el usuario escribe "fin", terminamos la ejecución del programa
    if ejercicio.lower() == "fin":
        break

    # Ejecutamos dinámicamente la función correspondiente al ejercicio seleccionado
    eval(f"Ejercicio{ejercicio}()")