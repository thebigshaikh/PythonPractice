myList=[1,2,3,4,5,6,7,8,1,2,3]
newList=[]
for elements in myList:
    if(elements<5):
        newList.append(elements)
print(sorted(newList))

uinput=int(input("enter a number \n"))
mlist=[]
for elements in myList:
    if(elements<uinput):
        mlist.append(elements)

print(set(mlist))