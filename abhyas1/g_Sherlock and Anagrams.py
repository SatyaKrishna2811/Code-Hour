q = int(input().strip())

for _ in range(q):
    s = input().strip()
    
    substring_counts = {}
    
    # Iterate over all possible lengths of substrings
    for length in range(1, len(s) + 1):
        # Iterate over all starting positions for the current length
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            # Sort the substring to identify anagrams easily
            sorted_sub = ''.join(sorted(sub))
            
            # Count the occurrences of each sorted substring
            substring_counts[sorted_sub] = substring_counts.get(sorted_sub, 0) + 1
            
    anagram_pairs = 0
    # Calculate the number of pairs for each anagram group combinations (nC2)
    for count in substring_counts.values():
        anagram_pairs += (count * (count - 1)) // 2
        
    print(anagram_pairs)