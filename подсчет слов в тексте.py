with open('dataset_3363_2.txt', 'r') as f:
    s = sorted(f.read().lower().split())
    most_common = None
    qty_most_common = 0
    for item in s:
        qty = s.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    print(most_common, qty_most_common)










