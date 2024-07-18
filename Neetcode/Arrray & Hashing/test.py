x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = dict(sorted(x.items(), key=lambda item: item[1]))

print(sorted_dict)