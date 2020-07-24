#10. merge the contents of any number of files specified by the user and produce a single file.

import shutil

n=int(input("How many files? "))
f=[]
reader=[]

for i in range(1,n+1):
    source=input("Enter the name of file : ")
    f= open(source,'r')
    r=f.read().split('\\n')
    reader.append(r)
    f.close()

print(reader)

des=input("Enter the destination: ")
with open(des,"w") as w:
    w.write(' '.join(reader))
w.close()






