a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

alice_score = 0
bob_score = 0

for i in range(3):
    if a[i] > b[i]:
        alice_score += 1
    elif a[i] < b[i]:
        bob_score += 1

result = [alice_score, bob_score]
print(*result)