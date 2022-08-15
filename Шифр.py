letter = [char for char in "abcd"]
key_word = [i for i in "*d%#"]
word = "abacabadaba"
word2 = "#*%*d*%"
dict1 = dict(zip(letter,key_word))
dict2 = dict(zip(key_word,letter))
output = []
output2 = []
res = ""
res2 = ""
for char in word:
    if char in dict1:
        char = dict1.get(char)
        output.append(str(char))
res = res.join(output)


for char in word2:
    if char in dict2:
        char = dict2.get(char)
        output2.append(str(char))
res2 = res2.join(output2)

print(res)
print(res2)

