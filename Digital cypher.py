alphabet = {'a': 1, 'b': 2, 'c':3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o':15, 'p': 16, 'q': 17, 'r': 18, 's': 19, ''
            't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

# letter = 'scout'
# lst_letter = list(letter)
# cypher = []
# key = [1,9,3,9]
# for i in lst_letter:
#     if i in alphabet:
#         cypher += [alphabet.get(i)]
# print(cypher)
#
#
# for i in range(0,len(cypher),4):
#     cypher[i] += key[0]
# for i in range(1,len(cypher),4):
#     cypher[i] += key[1]
# for i in range(2,len(cypher),4):
#     cypher[i] += key[2]
# for i in range(3, len(cypher), 4):
#     cypher[i] += key[3]

    # [20, 12, 18, 30, 21]

# print(cypher)


def encode(message, key):
    lst_message = list(message.lower())
    cypher = []
    lst_key = [int(i) for i in str(key)]


    for i in lst_message:
        if i in alphabet:
            cypher += [alphabet.get(i)]

    x = 0

    for i in range(len(cypher)):
        cypher[i] += lst_key[x]
        x += 1
        if x >= len(lst_key):
            x = 0

    # for i in range(1, len(cypher), 4):
    #     cypher[i] += lst_key[1]
    # for i in range(2, len(cypher), 4):
    #     cypher[i] += lst_key[2]
    # for i in range(3, len(cypher), 4):
    #     cypher[i] += lst_key[3]

    return cypher

print(encode('scout', 1939))
# [20, 12, 18, 30, 21]

# code = 1939
# new_code = [int(i) for i in str(code)]
# print(new_code)