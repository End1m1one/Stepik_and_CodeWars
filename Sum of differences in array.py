def sum_of_differences(arr):
    if len(arr) ==  0:
        return 0
    elif len(arr) == 2:
        summa = max(arr) + abs(min(arr))
        return abs(summa)

    else:
        el_max = max(arr)
        el_min = min(arr)
        el_eq = sum(arr) - el_max - el_min
        return ((el_max - el_eq) + (el_eq - el_min))



print(sum_of_differences([1, 2, 10]), 9)
print(sum_of_differences([-3, -2, -1]), 2)
print(sum_of_differences([1, 1, 1, 1, 1]), 0)
print(sum_of_differences([9, 21]), 21)
print(sum_of_differences([]), 0)
print(sum_of_differences([0]), 0)
print(sum_of_differences([-1]), 0)
print(sum_of_differences([1]), 0)