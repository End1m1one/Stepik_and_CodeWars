a = '17a189B'
g = list(a)
c = []
new = ''
for i in range(len(g)-1) :
    if g[i] not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' and g[i+1] not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' :
        g[i] += g[i+1]

print(g)
# for i in g:
#     if i not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
#         c.append(int(i))
#         g.remove(i)
# for i in g:
#     if i not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
#         g.remove(i)
# for i in range(len(g)):
#     new += c[i] * g[i]
# print(new)
# print(c)
# print(g)

# c = []
# g =[]
# for i in range(len(a)):
#     if a[i].isalpha():
#         c.append(a[i])
#     else:
#         g.append(a[i])
# print(c)
# print(g)

