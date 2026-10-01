import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    d = int(input_data[1])
    arr = [int(x) for x in input_data[2:2+n]]
    
    elements_set = set(arr)
    count = 0
    
    for x in arr:
        if (x + d in elements_set) and (x + 2 * d in elements_set):
            count += 1
            
    print(count)
