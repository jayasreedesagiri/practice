n=int(input("enter"))
factors=0
for i in range(2,n+1):
    if(n%i==0):
        factors+=1
if(factors==1):
    print("prime")
else:
    print("not prime")
