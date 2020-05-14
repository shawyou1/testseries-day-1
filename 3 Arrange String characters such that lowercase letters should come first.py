n=input()
if n.isalpha(): 
    b=list(n)
    b.sort()
    l,u=[],[]
    for i in b:
        if i.islower():
            l.append(i)
        if i.isupper():
            u.append(i)
    l="".join(sorted(l))
    u="".join(sorted(u))
    print("arranging characters giving precedence to lowercase letters \n",l+u)
    print("arranging characters giving precedence to lowercase letters: \n",u+l)
else:
    print("enter alphabets only")
