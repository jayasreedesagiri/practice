#Fibonacci series

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1)+fibo(n-2))

nterms=10
for i in range(nterms):
       print(fibo(i),end=" ")
print("\n")

#factorial
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = 7

#sort--
l=[3,6,9,1]
n=len(l)
for i in range(0,len(l)):
    for j in range(0,n-1-i):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)


#reverse--
l=[1,2,3,4,5]
n=len(l)
for i in range(0,n//2+1):
    l[i],l[n-i-1]=l[n-i-1],l[i]
print(l)


#pair of integers(sum) leading to k--
l=[1,2,3,4,5]
k=9
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]+l[j]==k):
            print(l[i],l[j])


#reverse string--
l=['a','b','c']
def rev(l):
    if(len(l)==1):
        return l[len(l)-1]
    else:
        return (l[len(l)-1]+rev(l[:len(l)-1]))
x=rev(l)
print(x)


#reverse list--
l=[1,2,3,4,5]
l=list(map(str,l))
def rev(l):
    if(len(l)==1):
        return l[len(l)-1]
    else:
        return (l[len(l)-1]+rev(l[:len(l)-1]))
x=rev(l)
print(x)


#reverse a string--
l="apple"
def rev(l):
    if(len(l)==1):
        return l[len(l)-1]
    else:
        return (l[len(l)-1]+rev(l[:len(l)-1]))
x=rev(l)
print(x)


#sum of numbers--
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
x=sum(5)
print(x)


#2-pointer approach(leading to k)--
l=[1, 2, 3, 4, 5, 6, 7]
l=sorted(l)
k=6
i=0
j=len(l)-1

while i<=j:
    if l[i]+l[j]==k:
        print(l[i],l[j])
        print(l[j],l[i])
        i=i+1
    elif l[i]+l[j]<k:
        i=i+1
    else:
        j=j-1


#Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped=True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
print("\n")



#binary search.
def binary_search(arr, low, high, x):
	if high >= low:

		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")


#linear search
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

#merge sort
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is")
	printList(arr)
	mergeSort(arr)
	print("\nSorted array is ")
	printList(arr)

