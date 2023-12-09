seqs = [[int(x) for x in line.strip().split(' ')]
        for line in open('9.txt')]

# part 1
ans = 0
for seq in seqs:
    hist = [seq]
    while not all(el == 0 for el in hist[-1]):
        diffs = []
        for i in range(len(hist[-1]) - 1):
            diffs.append(hist[-1][i + 1] - hist[-1][i])
        hist.append(diffs)
    ans += sum(lst[-1] for lst in hist)
print(ans)

# part 2
ans = 0
for seq in seqs:
    hist = [seq]
    while not all(el == 0 for el in hist[-1]):
        diffs = []
        for i in range(len(hist[-1]) - 1):
            diffs.append(hist[-1][i + 1] - hist[-1][i])
        hist.append(diffs)
    ans += sum(lst[0] * (-1)**i for i, lst in enumerate(hist))
print(ans)
