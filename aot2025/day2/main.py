ans = 0

def solve(l):
    global ans
    line = l[0]
    line.strip()

    separated = line.split(",")
    for r in separated:
        ranges = r.split("-")
        l,r 

    return ranges


with open("input.txt") as f:
    l = f.readlines()
    solve(l)

print(solve(l))
