def countbeauty(*args):
    f=open("//countWords.txt",'r')
    s=f.read()
    counts=dict()
    s.rstrip()
    s.lstrip("\n")
    names=s.split()
    for name in names:
        if name in counts:
            counts[name]+=1
        else:
            counts[name]=1

    print(counts)

    print("The occurence of beautiful is:{}".format(counts['beautiful']))

countbeauty()
