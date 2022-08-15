d = int(input("Кол-во слов:"))
lst = []
errors_lst = []
errors = []
for i in range(d):
    word = input("Введите слово:").lower()
    lst.append(word)
print(lst)

l = int(input("Кол-во строк:"))
for i in range(l):
    err = input("Введите текст:").lower().split()
    for char in err:
        if char not in lst:
            errors.append(char)


print(set(errors))


# print(errors)


