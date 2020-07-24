#6. fibonacci series till the Nth term by using a recursive function.

def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

n=int(input("How many numbers: "))
print("Fibonacci series: ")
for i in range(n):
    print(fibo(i))
