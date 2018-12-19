import random
list=[]


def randomNum():
    for i in range(4):
        r=random.randint(0,9)
        list.append(r)
    print(list)

randomNum()
uinput=input(" Enter your guess \n ")
print(uinput)

for i in uinput:
    print(i)
    if i in list:
        print(i)