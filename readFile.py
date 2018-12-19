

count=0
f=open("basil.txt","r")
c="cemetery"
resList= []


for line in f.readlines():
    slist=[line.split("/") ]
    if len(line.split("/")) > 1:
        print(line.split("/")[2])
        resList.append(line.split("/")[2])
f.close()
f1=open("basil.txt","r")



print(" Printing resList now")
print(resList)
resSet=set(resList)
resList=list(resSet)
print("Printing resSet")
print(resSet)
print(" Printing resList again")
print(resList)


for line1 in f1.readlines():
    for i in resList:
        if line1.find(i) != -1:
            count+=1





print("BasketBall count is ",count)

print(resList[0])

