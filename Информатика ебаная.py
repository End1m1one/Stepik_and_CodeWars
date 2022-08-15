import random

a = [2,5,6,7]
z = 0
print(min(a)*min(a))
for i in range(len(a)):
    if a[i] % 2 == 0:
       a[i] = min(a) * min(a)
       z += 1

print(z)
print(a)