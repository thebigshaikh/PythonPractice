list1=[1,2,3,4,3,7,9,0,5]
list2=[0,1,9,0,1,3,8,4,7,2,9,5,"basil"]
rlist=[]
for i in list2:
    for j in list1:
        if(i==j):
            rlist.append(i)

print(set(rlist))