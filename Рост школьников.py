dictt =  { }
n = 0
with open("Рост шокльников.txt", "r") as file:
    s =file.read().split()
    for char in s:
        if char.isalpha():
            s.remove(char)

    for i in range(len(s)):
        if s[i] == "1":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('1',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "2":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('2',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "3":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('3',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "4":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('4',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "5":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('5',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "6":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('6',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "7":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('7',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "8":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('8',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "9":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('9',[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "10":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault("10",[]).append(int(s[i+1]))
    for i in range(len(s)):
        if s[i] == "11":
            s[i] = int(s[i])
            n += 1
            dictt.setdefault('11',[]).append(int(s[i+1]))
for i in range(1,12):
    print(i, sum(dictt[str(i)])/len(dictt[str(i)]))