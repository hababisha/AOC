ans = [0]
dial = [50]
def solve(l):
    for line in l:
        line = line.strip()
        if not line: continue
        if line[0] == "L":
            dial[0] = (dial[0] - int(line[1:]))%100
        else:
            dial[0] = (dial[0] + int(line[1:]))%100
        if dial[0] == 0:
            ans[0] += 1

with open("input.txt") as f:
    l = f.readlines()
    solve(l)

print(ans[0])