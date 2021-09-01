import time

#Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 
# 00:00:00 do dia 1 de janeiro de 1970.
epoch_time = time.time() 

print(epoch_time)

#Uma string representando o horário local, calculado a partir do número de 
# segundos passado como parâmetro.
print(time.ctime()) 

#Converte o número de segundos em um objeto struct_time descrito a seguir.
print(time.gmtime())

#Semelhante à gmtime(), mas converte para o horário local.
print(time.localtime())
print(f'Data de hoje: {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year} {time.localtime().tm_zone}')

'''
Índice / Atributo / Valores
   0	   tm_year	   Por exemplo, 2020
   1	   tm_mon	   range [1, 12]
   2	   tm_mday	   range [1, 31]
   3	   tm_hour	   range [0, 23]
   4  	tm_min	   range [0, 59]
   5	   tm_sec	   range [0, 61]
   6	   tm_wday	   range [0, 6], Domingo é 0
   7	   tm_yday	   range [1, 366]
   8	   tm_isdst	   0, 1 ou -1
   N/A	tm_zone	   abreviação do nome da timezone
'''


#A função suspende a execução por determinado número de segundos.
print("Iniciou...")
time.sleep(3)
print("... terminou depois de 3 segundos.")