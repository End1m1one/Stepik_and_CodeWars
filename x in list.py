lst = [int(i) for i in input().split()]
x = int(input())
new_list = []
for i in range(len(lst)):
    if lst[i] == x:
        new_list.append(i)
print(*new_list)
if new_list == []:
    print("Отсутсвтует")

