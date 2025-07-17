import re    # llamamos al modulo de re (regular expressions)


                #-------- SEARCH ---------#

'''
La función re.search() se utiliza para buscar la primera ocurrencia 
del patrón en cualquier parte de la cadena. A diferencia de re.match(), 
re.search() no requiere que el patrón coincida desde el principio de la 
cadena.
'''

my_string = "Thiago es mi hijo y soy muy feliz de ser su padre"

my_search = re.search("feliz", my_string, re.I)
print(my_search)
print(my_search.span())

#----------------------------------------------------------------------

principio, fin = my_search.span()
print(my_string[principio:fin])

#----------------------------------------------------------------------




