s=input("enter a string:")
c=input("enter a char:")
count=0
for i in range(len(s)):
    if(s[i]==c):
        count+=1
print(count)
