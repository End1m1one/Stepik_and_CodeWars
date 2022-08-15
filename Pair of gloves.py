# def number_of_pairs(gloves):
#     dictt = {}
#     c = []
#     for i in gloves:
#             if i not in dictt:
#                 dictt[i] = [(gloves.count(i))]
#                 c.append(*dictt[i])
#     if sum(c) == len(c) +1:
#         return 1
#     elif sum(c) == len(c):
#         return 0
#     else:
#         return sum(c)//2
#     # print(len(c),sum(c))
#
# print(number_of_pairs(['Lime', 'Maroon', 'Silver', 'Lime', 'Olive']),1)
# print(number_of_pairs(["red","red"]),1)
# print(number_of_pairs(["red","green","blue","black"]),0)
# print(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
# print(number_of_pairs([]),0)
# print(number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]), 4)
# print(5%2)
def number_of_pairs(gloves):
    count = 0
    gloves.sort()
    i = 0
    while i < len(gloves) - 1:
        if gloves[i] == gloves[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count

print(number_of_pairs(['Lime', 'Maroon', 'Silver', 'Lime', 'Olive']),1)
print(number_of_pairs(["red","red"]),1)
print(number_of_pairs(["red","green","blue","black", "red"]),1)
print(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
print(number_of_pairs([]),0)
print(number_of_pairs(["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]), 4)

# def cntgloves(arr, n):
#     # To store the required count
#     count = 0
#
#     # Sort the original array
#     arr.sort()
#     i = 0
#     while i < (n - 1):
#
#         # A valid pair is found
#         if (arr[i] == arr[i + 1]):
#             count += 1
#
#             # Skip the elements of
#             # the current pair
#             i = i + 2
#
#         # Current elements doesn't make
#         # a valid pair with any other element
#         else:
#             i += 1
#
#     return count
#
# print(cntgloves([2,2,2,2,3, 2,4,5,2],9))