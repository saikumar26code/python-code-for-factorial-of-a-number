#define a function
def factorial(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res
number=int(input("Enter the number :"))
print(factorial(number))