import re    # llamamos al modulo de re (regular expressions)


                #-------- SPLIT ---------#

'''
La función split() del módulo re en Python se utiliza para dividir 
una cadena en una lista, separándola en cada ocurrencia de un patrón 
especificado por una expresión regular. Es similar al método split() 
de las cadenas en Python, pero con la potencia adicional de usar 
expresiones regulares para definir los delimitadores.
'''

# en este ejemplo la ocurrencia que especificamos es la coma (,)
# split nos devuelve una lista separando cada valor según detecte
# la ocurrencia.

my_string = "1,2,3,4,5,6,7,8,9,10"

print(re.split(",", my_string))

#----------------------------------------------------------------------
