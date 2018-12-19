lf1=[]
lf2=[]
result=[]

f1=open("file1.txt","r")
f2=open("file2.txt","r")

for i in f1.readlines():
    lf1.append(i.rstrip('\n'))

for j in f2.readlines():
    lf2.append(j.rstrip('\n'))

print(lf1)
print(lf2)

for i in lf1:
    if i in lf2:
        result.append(i)
print(result)

f3=open("result.txt","a")
f3.write(str(result))
