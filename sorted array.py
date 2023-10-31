l=[15,14,25,14,32,14,31]
u=[]
for i in l:
    if i not in u and l.count(i)==1:
        u.append(i)
print(list(u))
