strs = ["act","pots","tops","cat","stop","hat"]
groups = {}
for string in strs:
    key = tuple(sorted(string))
    if key not in groups:
        groups[key] = []
    groups[key].append(string)
print(list(groups.values()))
