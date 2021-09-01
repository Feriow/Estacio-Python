import math
import my_lib

a = eval(input('Entre com o coeficiente a da equação: '))
b = eval(input('Entre com o coeficiente b da equação: '))
c = eval(input('Entre com o coeficiente c da equação: '))

delta = my_lib.calculaDelta(a,b,c)

print(f'O valor calculado de delta foi: {delta}')

#Cálculo raizes = (-b +- Raiz_quadradada(delta))/2a

if delta > 0:
   print('A equação tem 2 raízes reais.')
   raiz1 = (-b + math.sqrt(delta))/2*a
   raiz2 = (-b - math.sqrt(delta))/2*a
   print(f'As raízes da equação são {raiz1} e {raiz2}')
elif delta == 0:
   print('A equação tem 1 raíz real.')
   raiz1 = (-b + math.sqrt(delta))/2*a
   print(f'A raíz da equação é {raiz1}')
else:
   print('A equação não tem raíz real.')