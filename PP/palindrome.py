s=input("enter a string")
st=""
for i in range(len(s)-1,-1,-1):
    st+=s[i]
if(st==s):
    print("palindrome")
else:
    print("not palindrome")
