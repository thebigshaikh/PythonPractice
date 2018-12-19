
import random

a=random.sample(range(0,10),10)
ba=random.sample(range(7,15),5)
print(a)
print(ba)

res=[i for i in a if i in ba]
print(set(res))
