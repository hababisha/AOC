ans = 0
dial = 50

def solve(l):
    global ans, dial

    for line in l:
        line = line.strip()
        direction = line[0]
        dist = int(line[1:])

        if direction == "L":
            k = dial % 100
            if k == 0:
                k = 100
            if k <= dist:
                ans += 1 + (dist - k) // 100
            dial = (dial - dist) % 100
        else:
            k = (100 - dial) % 100
            if k == 0:
                k = 100
            if k <= dist:
                ans += 1 + (dist - k) // 100
            dial = (dial + dist) % 100


with open("input.txt") as f:
    l = f.readlines()
    solve(l)
    print(ans)
