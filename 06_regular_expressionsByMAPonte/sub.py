import re    # llamamos al modulo de re (regular expressions)


                #-------- Sub ---------#
'''
La función sub() en el módulo re de Python se utiliza para buscar 
todas las ocurrencias de un patrón de expresión regular en una cadena 
y reemplazarlas con una nueva cadena. Es una herramienta poderosa 
para realizar sustituciones basadas en patrones complejos.
'''
# SINTAXIS: re.sub(pattern, repl, string, count=0, flags=0)

# EJEM:1
my_string = "1,2,3,4,5,6,7,8,9,10"

print(re.sub("5","five",my_string, re.I))

#----------------------------------------------------------------------
# EJEM:2

my_string = "Thiago es mi hijos y soy muy feliz de ser su padre"

print(re.sub("Thiago es mi","Thiago y Azai son mis",my_string, re.I))


#----------------------------------------------------------------------
# EJEM:3

my_range = ", ".join(str(num) for num in range(1,51))

print(my_range)
print(my_range.find("5"))

# podemos personalizar el patrón de la busqueda 
print(re.sub("[0-1]","n", my_range))

