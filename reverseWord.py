str= "Test string"

def reverse(string):
    y=string
    print(y)
    result=[]
    for word in range(len(y)-1,-1,-1):
        print(y[word])
        result.append(y[word])
    print(result)
    print("".join(result))

reverse(str)
