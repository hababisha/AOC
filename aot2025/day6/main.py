input = []
ans = 0

with open("input.txt") as f:
    while True:
        l = f.readline()
        l = l.rstrip("\n")
        if not l:
            break 
        input.append(l.split())

y = 0

rows= len(input)
cols = len(input[0])

for j in range(cols):
    op = input[-1][j]
    isAdd = True
    cur = 0

    if op == "*":
        isAdd = False
        cur = 1

    for i in range(rows-1):
        val = int(input[i][j])

        if isAdd: cur += val
        else: cur *= val
    ans += cur

print(ans)