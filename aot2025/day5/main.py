freshRanges = []
ans = 0

def solve(num):
    global ans, freshRanges

    for a, b in freshRanges:
        a, b = int(a),int(b)
        if num < a:
            continue
        if num > b:
            continue

        ans += 1
        break

flag = 0
with open("input.txt", "r") as f:
    while True:
        if flag > 1:
            break
        line = f.readline()
        l = line.strip()
        if not l:
            flag += 1
            continue
        if not flag:
            l = l.split("-")
            freshRanges.append(l)
        if flag == 1:
            solve(int(l))
print(freshRanges)
print(ans)