def horizontal():
    print("___" * uinput)

def vertical():
    print("  |" * (uinput))

uinput=int(input("Enter the board size? \n"))

for i in range(uinput):
    horizontal()
    vertical()
horizontal()
