def calculaDelta(coef1, coef2, coef3):
   #Delta da equação de 2º grau = b^2 - 4ac
   global delta
   delta = coef2*coef2 - 4*coef1*coef3

delta = 0

a = eval(input('Entre com o coeficiente a da equação: '))
b = eval(input('Entre com o coeficiente b da equação: '))
c = eval(input('Entre com o coeficiente c da equação: '))

calculaDelta(a,b,c)

print(f'O valor calculado de delta foi: {delta}')

if delta > 0:
   print('A equação tem 2 raízes reais.')
elif delta == 0:
   print('A equação tem 1 raíz real.')
else:
   print('A equação não tem raíz real.')