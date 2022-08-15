# a = [int(i) for i in input().split()]
# summa = 0
# sqr = 0
# for i in a:
#     summa += i
#     sqr += i * i
#     if summa == 0:
#         print(sqr)
#

a = []
summa = 0
while True:
    a +=[int(i) for i in input().split()]
    if sum(a) == 0:
            for i in a:
                summa += i * i
            break

print(summa)

