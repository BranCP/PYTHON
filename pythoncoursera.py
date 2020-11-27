
import re

h=open("regex_sum_1077889.txt","r")

listafinal=list()
for linea in h:    
    y=re.findall('[0-9]+',linea);
    if len(y)!=0:
        listafinal=listafinal + y;
        
suma=0

for i in listafinal:
    suma=suma+int(i);

print(suma)