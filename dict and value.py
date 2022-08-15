def update_dictionary(d, key, value):
    if key in d:
        d.setdefault(key,[]).append(value)
    elif key not in d:
        d.setdefault(2*key,[]).append(value)
    elif 2*key not in d:
         d.fromkeys(2*key[value])


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)


# dic = {1:[24]}
# dic[1] += [2]
# print(dic)