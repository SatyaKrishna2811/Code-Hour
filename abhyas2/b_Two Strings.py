import sys

lines = sys.stdin.read().splitlines()
if lines:
    p = int(lines[0])
    idx = 1
    for _ in range(p):
        s1 = lines[idx]
        s2 = lines[idx+1]
        idx += 2
        if set(s1) & set(s2):
            print("YES")
        else:
            print("NO")