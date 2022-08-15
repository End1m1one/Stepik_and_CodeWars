list1 = [int(i) for i in input().split()]
new_list = sorted(list1)
sort_list=[]
if len(list1)==1:
    print()
else:
 for i in range(len(list1)):
    if i<len(list1)-1:
     if new_list[i] == new_list[i+1]:
        sort_list += [new_list[i]]
 print(*set(sort_list))


# for i in range(len(a)):
#         if i < len(a)-1:
#             s += [a[i-1] + a[i+1]]
#         else:
#             s += [a[0]+a[-2]]