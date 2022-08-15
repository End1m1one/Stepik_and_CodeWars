a = [int(i) for i in input().split()]
s = []
if len(a) == 1:
    print(*a)
elif len(a) == 2:
    s = [2 * a[-1], 2 * a[0]]
    print(*s)
else:
    for i in range(len(a)):
        if i < len(a)-1:
            s += [a[i-1] + a[i+1]]
        else:
            s += [a[0]+a[-2]]

    print(s)

#
# list1 = [int(i) for i in input().split()]
#
# if len(list1) == 1:
#     print(list1[0])
#
# elif len(list1) == 2:
#     print(list1[1]*2, list1[0]*2)
#
# else:
#     for i in range(len(list1)):
#         if i < len(list1) - 1:
#             print(list1[i-1] + list1[i+1], end=" " )
#         else:
#             print(list1[0] + list1[i-1])