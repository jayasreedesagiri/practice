l=list(map(int,input("enter").split()))
min_element=l[0]
for i in range(len(l)):
    if l[i]<min_element:
        min_element=l[i]
print(min_element)
