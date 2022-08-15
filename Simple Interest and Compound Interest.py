# p = 100
# r = 0.1
# n = 2
#
# S = p + r*100 * n
# print(int(S))
#
# Compaound = p*(1+r)**n
# print(int(Compaound))

def interest(p, r, n):
    Simple = p*(1 +r*n)
    Compaound = p * (1 + r) ** n
    return [round(Simple), int(Compaound)]

print(interest(5048, 0.4, 44),[200, 259])
