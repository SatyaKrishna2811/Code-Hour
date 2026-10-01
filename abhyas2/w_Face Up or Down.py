t = int(input().strip())

for _ in range(t):
    n, x = map(int, input().split())
    face_down = n - x
    print(min(x, face_down))
