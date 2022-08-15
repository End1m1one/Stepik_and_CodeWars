# TODO: Напишите программу, которая считывает со стандартного ввода целые числа,
# TODO: по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.



# summ = 0
#
# n = None
# while n != 0:
#     n =int(input())
#     summ += n
# print(summ)

# s = 0
# i = 1
# while i:
#     i = int(input())
#     s += i
# print(s)

# a = 7
# b = 5
# d = 1
# while   d % a !=0 or d % b!=0:
#     d = d+1
# print(d)
# print(1%a!=0)
#


s =0
while True:
    s = int(input())
    if s < 10:
        continue
    if s > 100:
        break
    print(s)
