n = int(input().strip())
gene = input().strip()

# Count the initial frequencies of each character in the string
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for char in gene:
    counts[char] += 1

target = n // 4

# If the gene is already steady, we need to replace 0 characters
if counts['A'] == target and counts['C'] == target and counts['G'] == target and counts['T'] == target:
    print(0)
else:
    min_len = n
    left = 0
    
    # Use a sliding window approach. 
    # 'right' expands the window, 'left' shrinks it.
    for right in range(n):
        # As a character enters our replacement window (left to right),
        # it is no longer part of the "outside" string, so we decrease its count.
        counts[gene[right]] -= 1
        
        # A window is valid if the remaining "outside" string has NO character 
        # exceeding the target limit. Once we have a valid window, we try to 
        # shrink it from the left side to find the smallest possible length.
        while (counts['A'] <= target and 
               counts['C'] <= target and 
               counts['G'] <= target and 
               counts['T'] <= target and 
               left <= right):
            
            # Record the minimum length found so far
            min_len = min(min_len, right - left + 1)
            
            # The character at 'left' exits the replacement window,
            # so we must add it back to the "outside" string count.
            counts[gene[left]] += 1
            left += 1
            
    print(min_len)