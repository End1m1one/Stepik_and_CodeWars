# name = 'Petr Ivanov'
# name = name.split()
# name.reverse()
# shuffler = " ".join(name)
# print(shuffler)

def name_shuffler(str_):
    name = str_.split()
    name.reverse()
    shuffler = " ".join(name)
    return shuffler
print(name_shuffler('Ivan Petrov'))