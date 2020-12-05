
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

import urllib.request, urllib.parse, urllib.error 
fhand = urllib.request.urlopen('http:/data.pr4e.org/romeo.txt')


for line in fhand:
    print(line.decode().strip())