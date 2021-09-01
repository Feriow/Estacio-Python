lista = [1, 2, 3, 4, 5]

def impares(iterable):
    lista_aux = []
    for item in iterable:
        if item % 2 != 0:
            lista_aux.append(item)
    return lista_aux

nova_lista = impares(lista)
print(nova_lista)

# Com filter()
def impar(item):
   return item % 2 != 0

nova_lista2 = list(filter(impar,lista))
print(nova_lista2)

# Com filter(lambda)
nova_lista3 = list(filter(lambda item: item % 2 != 0, lista))
print(nova_lista3)