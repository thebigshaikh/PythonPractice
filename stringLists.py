

testString=input("Insert a string to check \n")
strlena=len(testString)
x=''
for i in range(strlena):
    x=x+testString[strlena-1-i]
print(x)

if(testString==x):
    print("Palindrome")
else:
    print("Not a palindrome")

stringRev="".join(reversed(testString))
print(stringRev)
