#imprimir solo las letras a

for letra in "holanda":
    if (letra=="a"):
        print(letra);
        break;

#imprimir solo numeros pares

# for i in range(6):
#     if i%2==0:
#         print(i);


for i in range(6):
    if i%2!=0:
        continue;
    
    print(i);