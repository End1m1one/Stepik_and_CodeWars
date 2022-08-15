a = -5
b = 12
sr = 0
count = 0
for i in range(a,b+1):
    if i % 3 == 0:
        sr += i
        count += 1

print(sr/count)
print(sr)
print(count)
