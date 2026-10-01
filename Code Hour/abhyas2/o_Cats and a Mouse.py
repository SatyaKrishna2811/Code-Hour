import sys

data = sys.stdin.read().split()
if data:
    q = int(data[0])
    for i in range(1, q * 3, 3):
        x = int(data[i])
        y = int(data[i + 1])
        z = int(data[i + 2])
        
        dist_a = abs(x - z)
        dist_b = abs(y - z)
        
        if dist_a < dist_b:
            print("Cat A")
        elif dist_b < dist_a:
            print("Cat B")
        else:
            print("Mouse C")
