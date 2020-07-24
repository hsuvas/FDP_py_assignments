def calculateTotalSum(*args): 
    totalSum = 0
    for number in args: 
        totalSum += sum(number)
    print(totalSum) 
  
# function call
l=[]
s=int(input("How many numbers do you want to give?"))
for i in range(s):
    i=int(input("Enter the numbers:"))
    l.append(i)
calculateTotalSum(l)   
#calculateTotalSum(5, 4, 3, 2, 1) 
#calculateTotalSum(6, 5, 4, 3, 2, 1)
