s=input("enter string")
st=""
count=0
for char in s:
    if char not in st:
        count+=1
print(count)

