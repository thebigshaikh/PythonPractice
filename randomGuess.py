import random

number=random.randint(0,10)
print(number)



while True:
    uinput=input("Enter a number? \n")
    print(uinput)
    if uinput.isdigit():
        if int(uinput)==number:
            print("Woah You should be gambling!")
            break
        elif int(uinput)>number:
            print("AH too high")
        elif int(uinput)<number:
            print("Too low")
    elif uinput == "exit":
        break

