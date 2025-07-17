''' ### lista completa de los metacaracteres ###

Python tiene un paquete integrado llamado re, que puede usarse 
para trabajar con expresiones regulares.

    . ^ $ * + ? { } [ ] \ | ( )    
'''
import re

'''
findall: Retorna una lista que contiene todas las coincidencias.

search: Retorna un objeto Match si hay una coincidencia en cualquier parte de la cadena.

split: Retorna una lista donde la cadena ha sido dividida en cada coincidencia.

sub: Reemplaza una o muchas coincidencias con una cadena.
'''
#-----------------------------------------------------------

'''1: [ ]
Se utilizan para especificar una clase de carácter, que es un conjunto de caracteres 
que desea hacer coincidir. Los caracteres se pueden enumerar individualmente, o se 
puede indicar un rango de caracteres dando dos caracteres y separándolos con un '-'.
''' 

variable_1 = "a,b,c,d,e,f,g,h,i,j,k,f,a"

print(re.findall("[a-f]",variable_1))    #--> de esta manera nos imprime valores entre a y f


print(re.findall("[af]",variable_1))     # --> de esta manera nos imprime los valores tantas veces aparezca (numero ocurrencias)

#-----------------------------------------------------------
'''2: \\
El metacaracter ESCAPAR en expresiones regulares: Muchos caracteres tienen significados especiales 
(metacaracteres) que representan patrones específicos en lugar de caracteres literales. Si quieres usar 
uno de estos caracteres como un carácter literal en tu patrón de búsqueda, debes escaparlo con 
"\". Por ejemplo, si quieres buscar un punto literal ".", debes escribir "\." en tu patrón de expresión regular.

Indicar secuencias especiales: "\" también se usa para indicar secuencias especiales que representan caracteres 
con significados específicos, como "\d" para dígitos, "\s" para espacios en blanco, "\w" para caracteres 
de palabra, entre otros.
'''
# EJEM: ESCAPAR USADO PARA ANULAR CARACTER ESPECIAL.

variable_2 = "a,b,c,d,e,\\"  # --> \ al ser un caracter especial tenemos que escaparlo para que el programa lo lea como normal
print(variable_2)
print(variable_2[10])

# EJEM: ESCAPAR, USADO PARA LLAMAR SECUENCIA ESPECIAL "\d".

variable_3 = "1,2,3,4, miguel"


def busqueda(variable):
    caracteres = ""
    caracteres= re.findall("\d",variable)
    return caracteres

print(busqueda(variable_3))

#-----------------------------------------------------------
'''3: .
(punto) se utiliza para coincidir con cualquier carácter, excepto una nueva línea (\n). 
Esto significa que es un COMODÍN que puede representar cualquier letra, número, símbolo o 
espacio, siempre y cuando no sea un salto de línea.
'''
# EJEM.

texto = "12345"
patron = r"123.."

print(re.findall(patron, texto))

# EJEM.

texto = "Thiago"
print(re.findall("Thi...", texto))
#-----------------------------------------------------------
'''4: ^
Inicio de la cadena: Cuando se usa al principio de una expresión regular, el ^ indica 
que la coincidencia debe ocurrir al comienzo de la cadena.
'''

variable_ejem = "Me encantan las peliculas de harry potter"
variable_ejem_2 = "1,2,3,4,5,6,7"

busqueda_2 = re.findall("^Me", variable_ejem)
busqueda_3 = re.findall("^3",variable_ejem_2)



if busqueda_2 and busqueda_3:
    print("Sí hay coincidencias en ambos textos")
elif busqueda_2:
    print("Hay coincidencia en busqueda 2")
elif busqueda_3:
    print("Hay coincidencia en busqueda 3")
else:
    print("No hay coincidencias en general")

# en este ejemplo vemos como evalúa si en las dos variables creadas
# existen o nó coincidencias al comienzo del texto.
#-----------------------------------------------------------
'''5: $
El metacaracter $ en expresiones regulares en Python tiene la función de indicar el 
final de una cadena o el final de una línea si se usa con el modo multilínea.
'''

variable_ejem_4 = "Este ejemplo es para probar el metacaracter $"

busqueda_4 = re.findall("$", variable_ejem_4)

if busqueda_4:
    print("Hay coincidencia en busqueda 4")
else:
    print("No hay coincidencias")

#-----------------------------------------------------------
'''6: *
El metacaracter * en expresiones regulares en Python tiene la función de coincidir 
con el carácter o el grupo de caracteres que lo precede cero o más veces. Es un cuantificador
que indica que el elemento anterior puede aparecer ninguna, una o muchas veces.
'''

variable_ejem_5 = "0,1,2,3,4,5,6,7,8"

busqueda_5 = re.findall("0.*", variable_ejem_5)

print(busqueda_5)

#-----------------------------------------------------------
'''7: +
El metacaracter + en expresiones regulares en Python también es un cuantificador, pero a 
diferencia de *, que coincide con el carácter o grupo de caracteres que lo precede cero o 
más veces, + coincide con el carácter o grupo de caracteres que lo precede una o más veces. 
Esto significa que debe haber al menos una ocurrencia del elemento anterior para que la 
coincidencia sea válida.
'''

variable_ejem_6 = "0,1,2,3,4,5,6,7,8"

busqueda_6 = re.findall("0.+", variable_ejem_6)

print(busqueda_6)
#-----------------------------------------------------------
'''8: $
El metacaracter ? en expresiones regulares en Python se utiliza como un cuantificador que 
indica que el carácter o el grupo de caracteres que lo precede puede aparecer cero o una vez. 
Esto significa que el elemento anterior es opcional.
'''


txt = "hello planet"

x = re.findall("p?anet", txt)

print(x)

#-----------------------------------------------------------
'''9: {}
En las expresiones regulares, los corchetes {} tienen un significado específico y se utilizan
para cuantificar la repetición de caracteres, grupos o clases de caracteres. Aquí te explico 
los dos usos principales de los corchetes {} en expresiones regulares:

En resumen, los corchetes {} permiten especificar de manera precisa cuántas veces debe repetirse 
el elemento anterior en una expresión regular, lo cual es útil para definir patrones de búsqueda 
o validación concretos en cadenas de texto.
'''

variable_ejem_7 = "hola Thiago"

busqueda_7 = re.findall("hola.{7}", variable_ejem_7)

print(busqueda_7)
#-----------------------------------------------------------
'''10: |
En las expresiones regulares, el símbolo | se utiliza como operador OR, lo que significa que 
permite especificar alternativas dentro de un patrón de búsqueda.
'''

variable_ejem_8 = "hola Thiago"

busqueda_8 = re.findall("hola | Thiago", variable_ejem_8)

if busqueda_8:
    print("tenemos coincidencia")
else:
    print("no tenemos coincidencias")

#-----------------------------------------------------------



