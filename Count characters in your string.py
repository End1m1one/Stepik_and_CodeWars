def count(string):
    dict = {}
    for i in string:
        if i not in dict:
            dict.setdefault(i, string.count(i))
    return dict
