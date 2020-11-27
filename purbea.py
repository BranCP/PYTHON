fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
    
    

fh = open(fname)
count = 0
listafinal=list()

for line in fh:
    line.rstrip()
    if not line.startswith("From") : continue
    linea2=line.split()
    listafinal.append(linea2[1])
    count=count+1
    

for line in listafinal:
    print(line)
    
print("There were", count, "lines in the file with From as the first word")
