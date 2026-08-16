# Read the 6x6 2D array from input
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_sum = float('-inf')

# Iterate through the grid stopping at index 3 to prevent out-of-bounds errors
for i in range(4):
    for j in range(4):
        
        # Calculate the 7 values making up the hourglass shape
        current_hourglass_sum = (
            arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
            arr[i+1][j+1] +                          # Middle 
            arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
        )
        
        # Track the maximum sum found
        if current_hourglass_sum > max_sum:
            max_sum = current_hourglass_sum

print(max_sum)