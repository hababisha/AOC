freshRanges = []
processed = []

ans = 0

with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        l = line.strip()
        if not l:
            break
        l = l.split("-")
        freshRanges.append(l)

for a, b in freshRanges:
    processed.append([int(a), int(b)])

processed.sort()

minn, maxx = processed[0][0], processed[0][1]
prev = (maxx - minn) + 1   
ans = 0

for i in range(1, len(processed)):
    a, b = processed[i]
    preva, prevb = processed[i - 1]

    if a <= maxx:
        minn = min(minn, a)
        maxx = max(maxx, b)
        prev = (maxx - minn) + 1
    else:
        ans += prev
        minn, maxx = a, b
        prev = (maxx - minn) + 1

ans += prev

print(ans)
