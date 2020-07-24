#4. To return the number of blankspaces, consonants and vowels in a string taken as input from the user.

def blankspaces(s):
    count_b=0
    
    for i in s:
        if i==" ":
            count_b+=1
    print(count_b)

def vowels(s):
    count_v=0
    vowels=['a','e','i','o','u','A','E','I','O','U']

    for i in s:
        if i in vowels:
            count_v+=1 
    print(count_v)
    
def consonents(s):
    count_c=0
    vowels=['a','e','i','o','u','A','E','I','O','U']

    for i in s:
        if i not in vowels and (ord(i)>65 and ord(i)>90) or (ord(i)>97 and ord(i)>122):  #to keep the values inside ASCII character set
            count_c+=1 
    print(count_c)

    
s=input("enter the string")
blankspaces(s)
vowels(s)
consonents(s)
