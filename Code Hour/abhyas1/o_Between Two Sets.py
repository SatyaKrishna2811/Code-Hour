# --- Read Input ---
# First line contains sizes of the arrays (can be ignored for the main logic)
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

# Read the two arrays from the console
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))

# --- Main Logic ---
count = 0

# Set the optimal mathematical range boundaries
start = max(arr)
end = min(brr)

for i in range(start, end + 1):
    valid = True
    
    # Check if 'i' is a multiple of all elements in array 'arr'
    for num in arr:
        if i % num != 0:
            valid = False
            break
            
    # Check if 'i' divides all elements in array 'brr'
    if valid:
        for num in brr:
            if num % i != 0:
                valid = False
                break
                
    if valid:
        count += 1

# --- Normal Output ---
print(count)
