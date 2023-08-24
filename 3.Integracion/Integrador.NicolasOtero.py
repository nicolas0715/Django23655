# --------------------------------------------------------------------------------------------------------------------------- #
# 1.Escribir una funcion que calcule el maximo comun divisor entre dos numeros.

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("# 1.---------------------------------------------------------------------------------------------------- #")
print(mcd(40, 45))
print(mcd(50, 180))
print(mcd(26, 39))

# --------------------------------------------------------------------------------------------------------------------------- #
# 2.Escribir una Funcion que calcule el minimo comun multiplo entre dos numeros.

print("# 2.---------------------------------------------------------------------------------------------------- #")
def mcm(a, b):
    return a * b // mcd(a, b)

print(mcm(40, 45))
print(mcm(50, 180))
print(mcm(26, 39))

# --------------------------------------------------------------------------------------------------------------------------- #
# 3.Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

print("# 3.---------------------------------------------------------------------------------------------------- #")
def dictio(cadena):
    dic = {}
    for n in cadena.split():
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    return dic

print(dictio('Esto es un string de prueba.'))
print(dictio('Aca estoy probando con otro string...'))
print(dictio('Esta es una tercera prueba, donde se ingreso un texto mas largo y tambien donde se repiten algunas palabras. Espero que esta prueba salga bien, porque sino no llego a terminar.'))

# --------------------------------------------------------------------------------------------------------------------------- #
# 4.Escribir una funcion que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra funcion que reciba el diccionario generado con la funcion anterior y devuelva una tupla con la palabra mas repetida y su frecuencia.

print("# 4.---------------------------------------------------------------------------------------------------- #")
def repetida(diccionario):
    cont = 0
    clave = ' '
    for c,v in diccionario.items():
        if v > cont:
            cont = v
            clave = str(c)
    return cont, clave

print(repetida(dictio('Esta es una tercera prueba, donde se ingreso un texto mas largo y tambien donde se repiten algunas palabras. Espero que esta prueba salga bien, porque sino no llego a terminar.')))

# --------------------------------------------------------------------------------------------------------------------------- #
# 5.Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
    entero = int(input('Ingrese un numero entero: '))
    return entero

'''Iterativamente'''
print("# 4.---------------------------------------------------------------------------------------------------- #")
bucle = True
while bucle:
    try:
        get_int()
    except ValueError as v:
        print('ERROR:', v)
        valor = str(v.args[0]).split("'")
        print('El valor ingresado no es un numero entero: ', valor[1])
        print('Intentalo otra vez')
    else:
        print('Ese si es un numero entero!')
        bucle = False

'''Recursivamente'''
def get_int():
    try:
        entero = int(input('Ingrese un numero entero: '))
        return entero
    except ValueError as v:
        valor = str(v.args[0]).split("'")
        print('El valor ingresado no es un numero entero: ', valor[1])
        return get_int()

print('Perfecto! El numero ingresado es: ', get_int())

# --------------------------------------------------------------------------------------------------------------------------- #
# 6.Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    #Getters
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_dni(self):
        return self._dni

    #Setters
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser un valor positivo")
    
    def set_dni(self, nuevo_dni):
        self._dni = nuevo_dni
        
    #Mostrar
    def mostrar(self,):
        print('Nombre:', self._nombre)
        print('Edad:', self._edad)
        print('Documento:', self._dni)
    
    #Es mayor?
    def es_mayor(self,):
        return self._edad >= 18

persona1 = Persona('Jorge Piazza', 17, 14564927)
print("# 6.---------------------------------------------------------------------------------------------------- #")
print(persona1.mostrar()) #Este metodo esta imprimiendo un "None" en pantalla y nose porque
print(persona1.es_mayor())

# --------------------------------------------------------------------------------------------------------------------------- #
# 7.Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad
    
    def get_titular(self):
        return self._titular

    def get_cantidad(self):
        return self._cantidad
    
    def set_titular(self, nuevo_titular):
        self._titular = nuevo_titular
    
    def mostrar(self):
        print("Titular:", self._titular.get_nombre())
        print("Cantidad:", self._cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
            print(f"Se ha ingresado {cantidad} en la cuenta.")
        else:
            print("La cantidad debe ser un valor positivo.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self._cantidad >= cantidad:
                self._cantidad -= cantidad
                print(f"Se ha retirado {cantidad} de la cuenta.")
            else:
                print("Fondos Insuficientes.")
        else:
            print("Incorrecto. La cantidad debe ser un valor positivo.")

print("# 7.---------------------------------------------------------------------------------------------------- #")
cuenta1 = Cuenta(persona1, 1000.00)
cuenta1.mostrar()
cuenta1.ingresar(1200)
cuenta1.mostrar()
cuenta1.retirar(2000)
cuenta1.mostrar()

# --------------------------------------------------------------------------------------------------------------------------- #
# 8.Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
# Un constructor.
# Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad) 
        self._bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self._bonificacion

    def set_bonificacion(self, nueva_bonificacion):
        self._bonificacion = nueva_bonificacion
    
    def es_titular_valido(self):
        edad_titular = self.get_titular().get_edad()
        return 18 <= edad_titular < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)  
        else:
            print("No se puede retirar dinero. Titular no válido.")
    
    def mostrar(self):
        print("----- Cuenta Joven -----")
        super().mostrar()  
        print("Bonificación:", self._bonificacion, "%")
    
persona_joven = Persona('Santiago Piazza', 22, 12345678)
cuenta_joven = CuentaJoven(persona_joven, 1500.00, 5)

print("# 8.---------------------------------------------------------------------------------------------------- #")
cuenta_joven.mostrar()
cuenta_joven.retirar(200.0)
cuenta_joven.mostrar()