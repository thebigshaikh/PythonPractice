import random


def bsearch(nlist, uinput):
    start_index = 0
    last_index = len(nlist) - 1
    print(start_index, last_index)

    while True:
        middle_index = int((last_index - start_index) / 2)
        print(middle_index)

        middle_number = nlist[middle_index]

        if uinput == middle_number or uinput == nlist[start_index] or uinput == nlist[last_index]:
            return True
            break
        elif middle_index == start_index or middle_index == last_index or middle_index == 0:
            return False
            break
        elif middle_number > uinput:
            last_index = middle_index
            print("last indrex", last_index)
        else:
            start_index = middle_index
            print("start indrex", start_index)


a = random.sample(range(1, 30), 10)
b = set(a)
print(b)

usrinput = int(input(" Enter the number \n"))
if (bsearch(list(b), usrinput)):
    print(" Number exists")
    print(b)
    openfile = open("basil.txt", "a")
    openfile.write("\n{}".format(str(b)))
    openfile.close()
else:
    print(" Number doesnt exists")
    print(b)
