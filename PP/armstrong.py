# Write Python 3 code in this online editor and run it.
n=0
s=str(n)
l=list(map(int,s))
r=[]
for char in l:
    r.append(char*char*char)
print(r)
su=sum(r)
print(su)
if(su==n):
    print("armstrong")
else:
    print("not armstrong")
