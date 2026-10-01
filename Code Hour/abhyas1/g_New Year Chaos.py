t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    q = list(map(int, input().rstrip().split()))

    bribes = 0
    chaotic = False

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            chaotic = True
            break
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    if not chaotic:
        print(bribes)
