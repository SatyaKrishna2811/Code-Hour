t = int(input())

for _ in range(t):
    num_str = input().strip()
    
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    print(first_digit + last_digit)
