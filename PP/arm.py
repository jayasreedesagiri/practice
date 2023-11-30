n=int(input("enter"))
s=str(n)
l=list(map(int,s))
r=[]
for i in l:
    r.append(i*i*i)
print(r)
su=sum(l)
if(su==n):
    print("armstrong")
else:
    print("not armstrong")
    
