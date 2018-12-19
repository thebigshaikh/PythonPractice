import random

list1 = []
def randomNum():
    for i in range(4):
        r = random.randint(0, 9)
        list1.append(r)
    print(list1)


randomNum()
uinput = input(" Enter your guess \n ")
print(uinput)
li = [int(x) for x in str(uinput)]
countBull = 0
countCow = 0

def compare():
    for i in range(4):
        if listpip[i] == li[i]:
            countBull += 1
        elif li[i] in list1 and list1[i] != li[i]:
            countCow += 1
        print(" Number of bulls are {}".format(countBull))
        print("Number of cows are {}".format(countCow))

if(countBull==4):
    print(" Congrats You Got it")
else:
    compare()
