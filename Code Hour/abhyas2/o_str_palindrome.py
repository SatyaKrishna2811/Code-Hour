n = int(input().strip())
total_chocolates = 0

for _ in range(n):
    word = input().strip()
    if word == word[::-1]:
        total_chocolates += len(word)

print(total_chocolates)
