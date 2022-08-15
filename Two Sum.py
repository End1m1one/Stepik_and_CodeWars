# def two_sum(numbers, target):
#     resault = []
#     for i in range(len(numbers)):
#         two = target - numbers[i]
#         if two in numbers:
#             if len(resault) < 2:
#                 two = numbers.index(two,i+1)
#                 resault.append(i)
#                 resault.append(two)
#     return resault

def two_sum(numbers, target):
    for i in range(len(numbers) -1 ):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]

#
print(two_sum([1,2,3],4))