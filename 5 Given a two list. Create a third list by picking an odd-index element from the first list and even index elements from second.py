a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=a[0::2]
print("Element at odd-index positions from list one \n",a)
b=b[1::2]
print("Element at even-index positions from list two \n",b)
c=a+b

print("Printing Final third list\n",c)
