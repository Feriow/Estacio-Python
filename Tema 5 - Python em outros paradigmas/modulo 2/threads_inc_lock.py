from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
lock = Lock()
print_lock = Lock()

'''
Primeiramente, definimos a variável global lock utilizando o construtor lock(), 
também do módulo threading (linha 6). Depois, vamos utilizar essa trava para “envolver” a 
operação de incremento. Imediatamente antes de incrementar o contador, chamamos o método acquire() 
da variável lock (linha 12), de forma a garantir exclusividade na operação de incremento (linha 13).

Logo após o incremento, liberamos a trava utilizando o método release (linha 14). Com apenas essa 
modificação, garantimos que o resultado estará correto. Podemos verificar o resultado no console abaixo.
'''

def funcao_a(indice):
    global contador
    for i in range(100000):
        lock.acquire()
        contador += 1
        lock.release()
    print_lock.acquire()
    print("Termino thread ", indice)
    print_lock.release()

if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)