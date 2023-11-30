n=int(input("enter range"))
fib=[0,1]
for i in range(n-2):
    f=fib[-1]+fib[-2]
    fib.append(f)
print(fib)
