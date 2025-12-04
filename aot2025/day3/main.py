ans = 0

def solve(l):
    global ans
    maxx = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            maxx = max(maxx,int(l[i]+l[j]))
        
    ans += maxx


with open("input.txt", "r") as f:
    for l in f:
        line = l.rstrip("\n")
        solve(line)
print(ans)