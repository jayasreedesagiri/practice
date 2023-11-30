l=list(map(int,input("enter").split()))
c=count(0)
for char in l:
	if char==0:
		l.remove(0)
for i in range(0,c):
	l.append(0)
print(l)