                    #EXAMPLE 1


#define the function
def factorial(n):

    #including the conditional statements
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1

        #creating a while loop to iterate the elements from 1 to n
        while (n!=0):

            #storing the factorial value in fact variable
            fact=fact*n
            n=n-1
        return fact
number=int(input("Enter the number :"))
print(factorial(number))
