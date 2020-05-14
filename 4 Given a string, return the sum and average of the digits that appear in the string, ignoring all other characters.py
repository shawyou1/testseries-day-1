z=""
l=[]

sum_digit = 0
str1=input()
for x in str1:
    if x.isdigit():
        z+=x
        
        
    elif x.isalpha():  
        l.append(z)
        
        z="" 
   
    if x==str1[len(str1)-1]:
        l.append(z)
       
    
    
    

l=(" ".join(l)).split()
print(sum(map(int,l)))
print(sum(map(int,l))/len(l))
