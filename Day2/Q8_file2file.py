#8.copy a text from one file to another.

sfname=input("Enter the source file name: ")
dfname=input("Enter the destination file name: ")
with open(sfname,'r') as f:
    with open(dfname,'w') as f1:
        for line in f:
            f1.write(line)


    
