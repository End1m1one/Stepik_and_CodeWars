a = 1634
b= [int(i) for i in str(a)]
c = []
for j in b:
    j = j ** len(b)
    c.append(j)
if sum(c) == a:
    print(True)
print(len(b))
print(a)
print(sum(c))

def is_narcissistic(n):
    num = str(n)
    length = len(num)
    return sum(int(a) ** length for a in num) == n