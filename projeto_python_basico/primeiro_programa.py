nome = input('Entre com seu nome: ')

peso = eval(input('Entre com seu peso: '))
altura = eval(input('Entre com sua altura: '))

imc = peso / (altura**2)

print(f'{nome} seu IMC é: {imc:.5}')


"""
def multiplicador(numero):
   a = 2
   print(f"Dentro da função, a variável a vale: {a}")
   return a * numero

a = 3
b = multiplicador(5)
print(f"b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")
"""
"""
def multiplicador(numero):
   return a * numero

a = 3
b = multiplicador(5)
print(f"b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")
"""
"""
def multiplicador(numero):
   global a
   a = 2
   print(f"Dentro da função, a variável a vale: {a}")
   return a * numero

a = 3
b = multiplicador(5)
print(f"b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")
a = 3
print(f"Fora da função, a variável a vale: {a}")
"""