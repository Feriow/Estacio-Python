from threading import Thread
import time

# Exemplo de função com parâmatros
def funcao(mensagem):
   for i in range(3):
      print(i,mensagem)
      time.sleep(1)

print('Iniciando o programa!')
x = Thread(target=funcao,args=('Executando',))
x.start()
print('Finalizando o programa!')