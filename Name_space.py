def fake_bin(x):
    # comment
    res = ""
    for i in x:
        if int(i) < 5:
            i = "0"
        if int(i) >= 5:
            i = "1"
        res += res.join(i)
    return res
print(fake_bin("800857237867"))