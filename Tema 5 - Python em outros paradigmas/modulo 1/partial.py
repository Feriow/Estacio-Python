# Exemplo partial
import operator
from functools import partial
adiciona_um = partial(operator.add,1)

print(adiciona_um(5))

# Segundo exemplo: collections e tuplas sem partial
print('\nSegundo exemplo')
import collections
from operator import attrgetter
pessoa = collections.namedtuple('pessoa', 'nome idade')
pessoas = [pessoa('Joao',40), pessoa('Ana',20), pessoa('Renata',25)]

print(sorted(pessoas, key=attrgetter('nome')))
print(sorted(pessoas, key=attrgetter('idade')))

# Terceiro exemplo: collections e tuplas com partial
print('\nTerceiro exemplo')
sort_nome = partial(sorted, key=attrgetter('nome'))
sort_idade = partial(sorted, key=attrgetter('idade'))

print(sort_nome(pessoas))
print(sort_idade(pessoas))