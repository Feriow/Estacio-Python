#num = eval(input("Entre com um número inteiro: "))
#print(num)
'''
import math

root = math.sqrt(4)

print(root)

print(math.ceil(9.214))
print(math.floor(9.214))
print(math.cos(2*math.pi))
print(math.sin(math.pi/2))
print(math.log(10,10))
print(math.e)
print(math.pi)
'''

import random

seq = [1,2,3,4,5,6,7,8,9,0]

print(random.choice(seq))
seq2 = seq
print(seq2)
random.shuffle(seq2)
print(seq2)
print(random.sample(seq,3))