list1=list(map(int,(input().split()))) #list of number
for i in list(len(list1)-1,,-1): #for loop to print the list in reverse order 
    print(list1[i])
