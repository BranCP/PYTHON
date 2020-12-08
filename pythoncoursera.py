
# import re

# h=open("regex_sum_1077889.txt","r")

# listafinal=list()
# for linea in h:    
#     y=re.findall('[0-9]+',linea);
#     if len(y)!=0:
#         listafinal=listafinal + y;
        
# suma=0

# for i in listafinal:
#     suma=suma+int(i);

# print(suma)

#coinectarse con la intelné

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd ='GET http://data-pre4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True: 
#     data=mysock.recv(512)
#     if(len(data)<1):
#         break
#     print(data.decode())
    
# mysock.close()


# clase 12.4 retrieving web pages

# import urllib.request, urllib.parse, urllib.error 
# fhand=None
# text_to_check="romeo.txt"
# try:
#     fhand = urllib.request.urlopen('http://data.pr4e.org/'+ urllib.parse.quote(text_to_check))
# except Exception as e:
#     print("callo")
#     print(e)

# counts=dict()

# for line in fhand:
#     words=line.decode().split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1

# print(counts)

# import urllib.request, urllib.parse, urllib.error 
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# tarea de la clase scrpaing tarea 1



import urllib.request, urllib.parse, urllib.error
from code3.bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))