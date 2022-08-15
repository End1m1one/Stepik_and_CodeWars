# string = "CodeWars"
# odd = []
# even = []
# str_res = ""
# for i in range(0,len(string), 2):
#     odd.append(string[i])
# str_res = "".join(odd)
# str_res += "".join(" ")
# for i in range(1,len(string), 2):
#     even.append(string[i])
# str_res += "".join(even)
#
# print(str_res)



def sort_my_string(s):
    odd = []
    even = []
    str_res = ""
    for i in range(0, len(s), 2):
        odd.append(s[i])
    str_res = "".join(odd)
    str_res += "".join(" ")
    for i in range(1, len(s), 2):
        even.append(s[i])
    str_res += "".join(even)

    return str_res

print(sort_my_string("CodeWars"))