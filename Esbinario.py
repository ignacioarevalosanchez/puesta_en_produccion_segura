"""	Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que introduzca un número binario e imprima por pantalla el número en formato decimal. Para desarrollar el programa, es necesario que desarrolles una función con la siguiente cabecera:  
def esBinario(strbinario)  

# Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado como parámetro contiene una cadena binaria.  # Ejemplo de esBinario:  print(esBinario(“1001”))  True  
print(esBinario(“Hola”))  
False
"""


def esBinario (strbinario):
    try:
        for elemento in range (0,len(strbinario)):
            if strbinario[elemento]!='1' and strbinario[elemento]!='0':
                return False
        return True
    except TypeError:
        return False

def convertir (binario):
    try:
        decimal=0
        for elemento in range (0,len(binario)):
            if binario[elemento]=='1':
                decimal = decimal+pow(2, len(binario)-elemento-1)
        return decimal
    except TypeError:
        return False

cadena = str(input("Introduce un numero binario para convertirlo a decimal: "))

if esBinario(cadena):
    print (f"{cadena} el numero que has introducido es binario y corresponde al numero decimal : " + str(convertir(cadena)))
else:
    print (f"{cadena} el numero que has introducido no es binario")


