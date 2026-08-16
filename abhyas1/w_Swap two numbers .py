num = list(map(int, input().split()))

rev_num = num[::-1]
#start stop step
print(*rev_num)

# or

# Read three values from a single line
a, b, c = input().split()

# Swap to change order from (1, 2, 3) to (2, 1, 3)
temp = a
a = b
b = temp

# Print the final result
print(a, b, c)
