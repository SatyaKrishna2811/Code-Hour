import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
ranked = [int(x) for x in input_data[1:n+1]]
m = int(input_data[n+1])
player = [int(x) for x in input_data[n+2:n+2+m]]

unique_ranked = sorted(list(set(ranked)), reverse=True)
index = len(unique_ranked) - 1

for score in player:
    while index >= 0 and score >= unique_ranked[index]:
        index -= 1
    print(index + 2)
