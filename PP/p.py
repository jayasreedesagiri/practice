def factorial(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return n*factorial(n-1)
n=int(input("entr"))
print(factorial(n))
