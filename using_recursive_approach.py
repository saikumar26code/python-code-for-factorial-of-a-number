#define the recursive function
def factorial(n):

    #conditional statements
    return 1 if (n==1 or n==0) else n*factorial(n-1)

#declare the variable to access the above function
number=int(input("Enter the number :"))
print(factorial(number))