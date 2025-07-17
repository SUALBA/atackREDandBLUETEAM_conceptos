import re    # llamamos al modulo de re (regular expressions)


                #-------- Patterns ---------#
# creamos variable pattern donde le damos como valor el patron de
# búsqueda que queremos aplicar.

my_string = "Thiago es mi hijo y tiene 5 meses de vida "

pattern_1 = r"[T|t]hiago | hijo"

print(re.findall(pattern_1, my_string))

#----------------------------------------------------------------------
# EJEM
pattern_2 = r"[a-c]"   
print(re.findall(pattern_2, my_string))  # findall recorre y devuelve ocurrencias.

#----------------------------------------------------------------------
# EJEM
'''
re.search

- Busca el patrón en cualquier parte de la cadena de texto y 
devuelve el primer objeto Match que encuentre que coincida 
con el patrón.

- Si no encuentra ninguna coincidencia, devuelve None.
'''
pattern_3 = r"[1-6]"    
print(re.search(pattern_3, my_string))
#----------------------------------------------------------------------
# EJEM
'''
re.match

Busca el patrón solo al principio de la cadena de texto.
Si el patrón coincide al principio de la cadena, devuelve un objeto Match.
Si el patrón no coincide al principio de la cadena, devuelve None.
'''

def validar_num_españa(number):
    patron = r"^"
