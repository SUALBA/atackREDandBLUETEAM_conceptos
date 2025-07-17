import re    # llamamos al modulo de re (regular expressions)


                #-------- FINDALL ---------#

'''
La función findall() en el módulo re de Python se utiliza para 
encontrar todas las ocurrencias de un patrón en una cadena de texto. 
Devuelve una lista con todas las coincidencias encontradas.
'''

my_string = "Thiago es mi hijo y soy muy feliz de ser su padre"


findall = re.findall("soy muy feliz de ser su padre", my_string, re.I)
print(findall)

#----------------------------------------------------------------------

# en este ejemplo lo vemos mejor, busca ocurrencias y crea lista con ellas.
# con esto podemos verificar que se repite.

my_string_two = "hola que tal hola que tal hola que tal"


findall_two = re.findall("hola", my_string_two, re.I)
print(findall_two)

#----------------------------------------------------------------------

my_string_three = "1,2,3,4,5,1,2,3,4,5,1,2,3,4,5"


findall_three = re.findall("1", my_string_three, re.I)
print(findall_three)