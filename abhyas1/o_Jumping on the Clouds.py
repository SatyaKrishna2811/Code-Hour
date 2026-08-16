# Read the number of clouds
n = int(input().strip())

# Read the cloud array
c = list(map(int, input().rstrip().split()))

# Initialize variables
jumps = 0
i = 0

# Calculate the minimum jumps
while i < n - 1:
    if i + 2 < n and c[i + 2] == 0:
        i += 2
    else:
        i += 1
    jumps += 1

# Print the final result
print(jumps)
