def gps(s, x):
    speed = []
    for i in range(len(x) - 1):
        speed.append(x[i+1] - x[i])
    return int((max(speed)* 3600)//s)



print(gps(12, [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]))