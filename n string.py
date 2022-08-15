n = int(input())
string = []
b = []
for i in range(n+1):
    b += [str(i)] * i
print(*b[0:n])


# v = []
#
# for i in range(1, n+1):
#     v += [str(i)] * i
#
# print(" ".join(v[:n]))
