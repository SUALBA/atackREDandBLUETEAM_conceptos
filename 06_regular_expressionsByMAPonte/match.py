### Regular Expressions ###

# mecanismo o estandar de los lenguajes de programación
# que al usarlo nos permite verificar o inspeccionar si 
# una cadena de texto tiene o nó cosas. 

# Además es capaz de decirnos las ocurrecias en caso de tener datos,
# con las expresiones regulares.

import re    # llamamos al modulo de re (regular expressions)


                #-------- MATCH ---------#
'''
La función re.match() se utiliza para comprobar si el patrón 
coincide al comienzo de la cadena. Si el patrón no coincide desde 
el primer carácter de la cadena, re.match() devuelve None.
'''

my_string = "Thiago es mi hijo y soy muy feliz de ser su padre"


# este print nos dará None ya que match por defecto verifica el inicio del string.
print(re.match("soy muy feliz", my_string))

#----------------------------------------------------------------------

# en este print, match si reconoce el string por ser el comienzo.
# .span nos dice el rango del string que buscamos, desde posición o a 17.
# re.I se utiliza para realizar una búsqueda insensible a mayúsculas y 
# minúsculas en las expresiones regulares.
my_match = re.match("Thiago es mi hijo", my_string, re.I)
print(my_match) 
print(my_match.span()) 

#----------------------------------------------------------------------
# sabemos que .span nos dará dos valores, el principio y el fin del
# string que le dimos al match.

# sabiendo esto nos acordamos de las tuplas, las cuales usamos para
# guardar diferentes valores en diferentes variables.

# my_match.span() == (0,17)
# my_string[0:17]

principio, fin = my_match.span()
print(my_string[principio:fin])