# Read the number of test cases
T = int(input().strip())

for _ in range(T):
    # Read the size of the array
    N = int(input().strip())
    
    # Read the array elements
    A = list(map(int, input().strip().split()))
    
    # Generate and print all subarrays
    for i in range(N):
        for j in range(i, N):
            # Slice the array from the starting index 'i' to the ending index 'j'
            subarray = A[i:j+1]
            
            # Unpack and print the subarray elements separated by a space
            print(*subarray)