s=input("enter a string:")
s1=input("enter another string:")
count=0
if(len(s)==len(s1)):
    for char in s:
        if char in s1:
            count+=1
if(count==len(s)):
    print("anagram")
else:
    print("not anagram")

            
