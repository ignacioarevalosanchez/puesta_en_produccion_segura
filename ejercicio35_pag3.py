"""
3.	Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes cabeceras:  
 
def estaEnRango(valor, minimo, maximo)  
# 1º: Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo.  
def estaEnLista(valor, lista)  
# 2º: Devuelve True o False determinando si el valor está en la lista. 


"""

def estaEnRango (valor, minimo, maximo):

    try:
        if valor >= minimo and valor <= maximo:
            return True
        else:
            return False
    except IndentationError:
        return False

# 1º Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo. 

def estaEnLista(valor, lista):

    try:
        if valor in lista:
            return True
        else:
            return False
    except IndentationError:
        return False

# 2º: Devuelve True o False determinando si el valor está en la lista.
min=1
max=20
variable=int(input(f"introduce un valor entre {min} y {max}: "))
lista=[6,14,11,3,2,1,15,19]


if estaEnRango(variable, min, max):

    try:        
        if estaEnLista(variable, lista):
            print (f"el numero {variable} esta incluido en la lista")
        else:
            print (f"el numero {variable} esta incluido en el rango pero no en la lista")
    except IndentationError:
        print ("No ha funcionado")
else:
    print (f" el numero {variable} no esta incluido  entre {min} y {max}" )

