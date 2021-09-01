from threading import Thread
import time

# Sincronizando threads
ls = []

def contador1(n):
   for i in range(1,n+1):
      print(i)
      ls.append(i)
      time.sleep(0.4)

def contador2(n):
   for i in range(6,n+1):
      print(i)
      ls.append(i)
      time.sleep(0.5)


x = Thread(target=contador1,args=(5,))
x.start()

#x.join()

y = Thread(target=contador2,args=(10,))
y.start()

x.join() #O .join() é utilizado para fazer o programa aguarda a finalização das threads antes de continuar
y.join()

print(ls)