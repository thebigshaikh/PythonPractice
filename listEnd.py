list1=[1,2,3,4,5]
reslist=[]
def starend():
    reslist.append(list1[0])
    reslist.append(list1[len(list1)-1])
    print(reslist)

starend()