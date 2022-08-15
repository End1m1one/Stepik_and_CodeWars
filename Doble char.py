# s = '1234'
# for i in s:
#     i += i
#     print(i, end='')


def double_char(s):
    c = []
    n = ''
    for i in s:
        c.append(i*2)
    for j in c:
         n += j
    return n


print(double_char('1234'))