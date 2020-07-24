#7. to print the shortest and longest word in a string taken as input from the user.

def lenstring(s):
    l=s.split()
    long=l[0]
    short=l[0]
    for i in l:
        if len(i)>len(long):
            long=i
        if len(i)<len(short):
            short=i
    print("Shortest word: ",short)
    print("Longest Word: ",long)


s=input("Enter the string: ")
lenstring(s)
        
