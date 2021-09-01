import threading
import urllib.request
import time

start = time.time()
urls = ['http://www.google.com','http://www.apple.com','http://www.microsoft.com','http://www.bing.com']

def chama_url(url):
   req = urllib.request.urlopen(url)
   #response = urllib.urlopen(req)
   #the_page = response.read()
   print(f'{url} carregado em {time.time() - start}')

threads = [threading.Thread(target=chama_url,args=(url,)) for url in urls]

for thread in threads:
   thread.start()
for thread in threads:
   thread.join()

print(f'Ellapsed time: {time.time() - start}')