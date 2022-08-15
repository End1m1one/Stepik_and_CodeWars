

list = ['abc', 'a', 'bCd', 'bC', 'AbC', 'BC', 'BCD', 'bcd', 'ABC']
spisok = []
for i in list:
    if i not in spisok:
        spisok.append(i)
        print('{} {}'.format(max(i),list.count(max(i))))



print(6%6)