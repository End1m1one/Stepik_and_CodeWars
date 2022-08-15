data = []
with open('dataset_3363_2.txt', 'r', encoding="utf-8") as f:
    s = f.read().strip()
    l = len(s)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))

    sr_ball = []
    start = 0
    stop = 3
    while stop <= len(integ) + 1:
        sr_ball.append(sum(integ[start:stop])/3)
        print(*sr_ball)
        sr_ball = []
        start += 3
        stop += 3



    summ_math = []
    summ_math.append((sum(integ[::3])/(len(integ)/3)))

    summ_ph = []
    summ_ph.append(sum(integ[1::3]) / (len(integ) / 3))

    summ_russ = []
    summ_russ.append(sum(integ[2::3])/(len(integ)/3))


    print(*summ_math, *summ_ph , *summ_russ)
    # print(*summ_ph)
    # print(*summ_russ)
# math_values = []
# physics_values = []
# russian_values = []
# with open('dataset_3363_2.txt', 'r') as in_file:
#     for line in in_file:
#         current_line = line.strip().split(';')
#         math_values.append(int(current_line[1]))
#         physics_values.append(int(current_line[2]))
#         russian_values.append(int(current_line[3]))
# out_file = open('statistic.txt', 'w')
# for i in range(len(math_values)):
#     out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
# if len(math_values) > 0:
#     out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
#                    str(sum(physics_values) / len(physics_values)) + ' ' +
#                    str(sum(russian_values) / len(russian_values)))
# out_file.close()



# count, a1, b1, c1 = 0, 0, 0, 0
# with open('dataset_3363_2.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip().split(';')
#         a, b, c = int(line[1]), int(line[2]), int(line[3])
#         print((a+b+c)/3)
#         count += 1
#         a1 += a
#         b1 += b
#         c1 += c
# print((a1/count), (b1/count), (c1/count))
# s = input()
# word_list = s.split(';')
# num_list = []
#
# for word in word_list:
#     if word.isnumeric():
#         num_list.append(int(word))
#
# print(num_list)