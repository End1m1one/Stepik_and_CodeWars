n = int(input())
x = 0
y = 0
start = (x,y)
for i in range(n):
    coord = input().split()
    if coord[0] == "север" :
        y += int(coord[1])
    if  coord[0] == "юг":
        y -= int(coord[1])
    if coord[0] == "запад":
        x -= int(coord[1])
    if coord[0] == "восток":
        x += int(coord[1])
print(x,y)