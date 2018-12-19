a=[1,12,2,3,4,2]
res=[]

for i in a:
    if i not in res:
        res.append(i)
        a.remove(i)

print(res)

