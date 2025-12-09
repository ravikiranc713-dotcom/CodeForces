from math import gcd
r = input()
lr = [num for num in r.strip(' ')]
numr = []
mr = max(lr)
for i in range(int(mr),7):
    numr.append(i)

x=len(numr)
y=6
result = gcd(x,y)
x = x//result
y = y//result
print(f'{x}/{y}')