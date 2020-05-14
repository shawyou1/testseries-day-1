n=input()
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
print(l+u)
