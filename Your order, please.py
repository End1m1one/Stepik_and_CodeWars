def order(sentence):
    sentence = sentence.split()
    n= 1
    res = []
    while n != len(sentence) + 1:
        for char in sentence:
            for i in char:
                if i == str(n):
                    res.append(char)
                    n +=1♦
    return " ".join(res)
print(order("is2 Thi1s T4est 3a"))
