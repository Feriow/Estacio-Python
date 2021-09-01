#Paradigma imperativo - O programador diz como fazer
print('### PARADIGMA IMPERATIVO ###')
numeros = [1,2,3,4]
total = 0
for numero in numeros:
   total += numero
print('O total é', total)

print('\nsegundo exemplo')
if True:
   print('Tudo certo')
else:
   print('ops')

#Paradigma funcional - O que você quer fazer
print('\n### PARADIGMA FUNCIONAL ###')
print('O total é', sum(numeros))

print('\nsegundo exemplo')
print('Tudo certo' if True else 'ops')

#Operators e Reduce
print('\n### OPERATOR E REDUCE ###')
import operator
print('Adição de dois valores =',operator.add(10,20))

from functools import reduce
print ('Adição de múltiplos valores =',reduce(operator.add,[10,20,30]))
print ('Concatenação com reduce =',reduce(operator.concat,['Aprendendo reduce! ','Indo bem!']))