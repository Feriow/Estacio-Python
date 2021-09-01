from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("Termino thread ", indice)


if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", len(minha_lista))

'''
    Apesar da saída do script thread.py ter ficado confusa (já iremos retornar nesse problema), 
    observe que o número de itens da variável minha_lista muda durante a execução do programa 
    quando usamos thread e não muda quando usamos processos.

   Isso acontece, pois a área de memória das threads é compartilhada, ou seja, elas têm acesso 
   às mesmas variáveis globais. Em contrapartida, as áreas de memória dos processos não são 
   compartilhadas. Cada processo acaba criando uma versão própria da variável minha_lista.
'''