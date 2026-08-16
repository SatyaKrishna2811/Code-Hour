t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    
    count = 0
    for digit_char in str(n):
        d = int(digit_char)
        if d != 0 and n % d == 0:
            count += 1
            
    print(count)
