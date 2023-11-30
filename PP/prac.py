#number into list
n=int(input("enter"))
s=str(n)
l=list(map(int,s))
print(l)

r=[]
for i in range(len(l)-1,-1,-1):
    r.append(l[i])
print(r)

    
