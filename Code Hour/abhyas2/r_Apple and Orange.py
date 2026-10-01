s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = map(int, input().split())
oranges = map(int, input().split())

print(sum(1 for x in apples if s <= a + x <= t))
print(sum(1 for x in oranges if s <= b + x <= t))
