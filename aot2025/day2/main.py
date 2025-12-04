def invalid(x):
    s = str(x)
    n = len(s)
    if n % 2 != 0:  
        return False
    half = n // 2
    return s[:half] == s[half:]

total = 0

with open("input.txt", "r") as f:
    line = f.read().strip()  

ranges = line.split(",")

for r in ranges:
    if not r: 
        continue
    start, end = map(int, r.split("-"))
    for x in range(start, end + 1):
        if invalid(x):
            total += x

print(total)
