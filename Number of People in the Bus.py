def number(bus_stops):
    count = []
    res = 0
    for stops in bus_stops:
        for people in stops:
            count.append(people)
    for i in range(len(count)):
        if i == 0 or i % 2 == 0:
            res += count[i]
        else:
            res -= count[i]
    return res

print(number([[10, 0], [3, 5], [5, 8]]))


