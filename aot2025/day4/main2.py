ans = 0
grid = []
dirs = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]

def inbound(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def solve(grid):
    global ans, dirs

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count = 0
            if grid[r][c] != "@":
                continue
            
            for x, y in dirs:
                nx, ny = x + r, y + c
                if not inbound(nx,ny):
                    continue
                if grid[nx][ny] == "@":
                    count += 1
            if count < 4:
                ans += 1
                grid[r][c] = "x"
            


with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        grid.append(list(line))

for _ in range(len(grid)*len(grid[0])):
    solve(grid)
print(ans)
