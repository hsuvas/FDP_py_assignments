#5. factorial of a number by using a recursive function.

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n=int(input("Enter the number"))
f=fact(n)
print("Factorial is: ",f)
