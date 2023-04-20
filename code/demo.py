import itertools

combo = ["A", "B", "C", "D"]
pairs = list(itertools.combinations(combo, 2))

for pair in pairs:
    print(pair)


[["A", "B", "C"], ["C", "D"], ["A", "C", "E"]]