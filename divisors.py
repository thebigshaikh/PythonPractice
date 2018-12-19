uinput=int(input("Enter a number \n"))

myList=[]

try:
    for i in range(1,uinput):
        if(uinput%i==0):
            myList.append(i)
except ZeroDivisionError:
    print(myList)

myList.append(uinput)
print(myList)