# def parts_sums(ls):
#     resault = []
#     for i in range(len(ls)):
#         resault.append(sum(ls[i::]))
#     resault.append(0)
#     return resault
# print(parts_sums([1, 2, 3, 4, 5, 6]))


def parts_sums(ls):
    resault = []
    for i in ls:
        resault.append(sum(ls))
         ls = ls.remove(i)

    return resault

print(parts_sums([1, 2, 3, 4, 5, 6]))
