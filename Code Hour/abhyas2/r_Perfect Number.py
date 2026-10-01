n = int(input())
divisors_sum = sum(i for i in range(1, n) if n % i == 0)
if divisors_sum == n:
    print("Yes")
else:
    print("No")
