n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

min_score = scores[0]
max_score = scores[0]
    
min_breaks = 0
max_breaks = 0

for score in scores[1:]:
    if score > max_score:
        max_score = score
        max_breaks += 1
    elif score < min_score:
        min_score = score
        min_breaks += 1
        
result = [max_breaks, min_breaks]

print(*result)