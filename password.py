import random

def passwordGen():
    stringRand = random.sample([1,2,3,4,5,6,0,12,24,12,32,31,2],7)
    print(stringRand)
    print(str(stringRand))
    return  "".join(str(stringRand))

passwordGen()
print(passwordGen())