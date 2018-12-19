start=0
last=100
middle=50
counter=1

print(" Guess a number between 0 and 100")
condition = int(input("Is your guess " + str(middle) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) "))

while condition != 1:
    counter += 1

    if condition == 0:
        last = middle
    elif condition == 2:
        start = middle

    middle=int((start+last)/2)
    condition = int(input("Is your guess " + str(middle) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) "))

print("It took us {} guesses to get it right! Cheers!".format(counter))




