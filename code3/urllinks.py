# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# #clase
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# print(tags)
# for tag in tags:
#     print(tag.get('href', None))

#tarea 1

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('span')
# count=0
# sum=0
# for tag in tags:
#     if len(tag.contents[0])<1:
#         continue
#     count=count+1
#     sum=int(tag.contents[0])+sum;

# print(count)
# print(sum)


#tarea 2


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
contadorlimite=int(input("Enter count: " ))
position = int(input("Enter position: "))
print("Retrieving: ",url)

contador=1
while(contador<=contadorlimite):
    posicionini=1
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    
    for tag in tags:
        
        if posicionini==position:
            print("Retrieving: ",tag.get('href', None))
            url=tag.get('href', None)
            break
        
        posicionini+=1
    
    contador=contador+1


# # Retrieve all of the anchor tags
# tags = soup('span')
# count=0
# sum=0
# for tag in tags:
#     if len(tag.contents[0])<1:
#         continue
#     count=count+1
#     sum=int(tag.contents[0])+sum;

# print(count)
# print(sum)
