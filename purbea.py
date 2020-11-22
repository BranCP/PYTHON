# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    a1=line.find(0)
    a2=float(line[a1:].strip())
    total=total+a2
    count=count+1
    
print("Contar:",count," suma: ",total)