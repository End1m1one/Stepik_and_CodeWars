def are_coprime(n,m):
    first = [int(i) for i in range(1, n +1) if n % i == 0 ]
    second = [int(i) for i in range(1, m +1) if m % i == 0 ]
    conter = 0
    for i in first:
        if i in second:
            conter += 1
    if conter > 1:
        return False
    else:
        return True



print(are_coprime(20,27))