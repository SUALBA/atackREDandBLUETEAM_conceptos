### Metacaracteres Especiales ###

import re

'''
\A: Devuelve una coincidencia si los caracteres especificados están al principio de la cadena.
-----------------------------------------------------------------------------------------------------------
\b: Devuelve una coincidencia donde los caracteres especificados están al principio o al final de una palabra 
(la "r" al principio asegura que la cadena se trate como una "cadena cruda")
-----------------------------------------------------------------------------------------------------------
\B: Devuelve una coincidencia donde los caracteres especificados están presentes, pero NO al principio 
(o al final) de una palabra (la "r" al principio asegura que la cadena se trate como una "cadena cruda") r"\Bain"
-----------------------------------------------------------------------------------------------------------A
\d: Devuelve una coincidencia donde la cadena contiene dígitos (números del 0-9) 
-----------------------------------------------------------------------------------------------------------
\D: Devuelve una coincidencia donde la cadena NO contiene dígitos 
-----------------------------------------------------------------------------------------------------------
\s: Devuelve una coincidencia donde la cadena contiene un carácter de espacio en blanco 
-----------------------------------------------------------------------------------------------------------
\S: Devuelve una coincidencia donde la cadena NO contiene un carácter de espacio en blanco 
-----------------------------------------------------------------------------------------------------------
\w: Devuelve una coincidencia donde la cadena contiene cualquier carácter de palabra
(caracteres de la a a la Z, dígitos del 0-9, y el carácter guion bajo _) 
-----------------------------------------------------------------------------------------------------------
\W: Devuelve una coincidencia donde la cadena NO contiene ningún carácter de palabra 
-----------------------------------------------------------------------------------------------------------
\Z: Devuelve una coincidencia si los caracteres especificados están al final de la cadena 
'''

#\A:

my_variable = "Hola soy Miguel y tengo 32 años de edad"

busqueda_1 = re.findall("\AHola", my_variable)

if busqueda_1:
    print(f"El comienzo de la cadena de texto si coincide: {busqueda_1}")
else:
    print("El comienzo de la cadena no coincide")
#-----------------------------------------------------------------------------------------------------------

#\b:

busqueda_2 = re.findall(r"uel\b",my_variable)

if busqueda_2:
    print(f"Si tenemos coincidencias: {busqueda_2}")
else:
    print("No se han encontrado coincidencias")
#-----------------------------------------------------------------------------------------------------------

#\B:

busqueda_3 = re.findall(r"\Bñ",my_variable)

if busqueda_3:
    print(f"Si tenemos coincidencias {busqueda_3}")
else:
    print("No se han encontrado coincidencias")
#-----------------------------------------------------------------------------------------------------------

#\d:

busqueda_4 = re.findall("\d",my_variable)

if busqueda_4:
    print(f"Si tenemos coincidencias: {busqueda_4}")
else:
    print("No se han encontrado coincidencias")
#-----------------------------------------------------------------------------------------------------------

#\D:

busqueda_5 = re.findall("\D",my_variable)

mi_cadena = ""

for caracteres in busqueda_5:
    mi_cadena += caracteres

print(mi_cadena)
#-----------------------------------------------------------------------------------------------------------

# \s:

busqueda_6 = re.findall("\s",my_variable)

espacios = len(busqueda_6)

print(f"Tenemos {espacios} espacios en blanco")

#-----------------------------------------------------------------------------------------------------------

# \S:


busqueda_7 = re.findall("\S",my_variable)

espacios = len(busqueda_7)

print(f"Tenemos {espacios} espacios con caracteres en el string")

#-----------------------------------------------------------------------------------------------------------

# \w:

caracteres = "Miguel, Angel - 1234 _ ?!"

busqueda_7 = re.findall("\w",caracteres)

print(busqueda_7)

#-----------------------------------------------------------------------------------------------------------

# \W:

busqueda_8 = re.findall("\W",caracteres)

print(busqueda_8)

#-----------------------------------------------------------------------------------------------------------

# \Z:

coincidencia = True

busqueda_9 = re.findall("edad\Z",my_variable)

print(my_variable)

if busqueda_9:
    print(coincidencia)
else:
    print("El final no coincide")

#-----------------------------------------------------------------------------------------------------------


#EJEMPLO DE PRACTICA.

solicitud_email = input("Introduzca su correo electrónico:\n")

email = solicitud_email

patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[com|es]+$"

comprobacion = re.findall(patron, email)


try:
    if comprobacion:
        print("Mail correcto")
    else:
        print("ERROR: Mail incorrecto")
except Exception as e:
    print(f"Tenemos un error: {e}")
finally:
    print(f"{email} - verificado")

#-----------------------------------------------------------------------------------------------------------











