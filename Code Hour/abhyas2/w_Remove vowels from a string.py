S = input()

result = ""

for char in S:
    if char not in "aeiou":
        result += char

print(result)

#or

# S = input()

# result = "".join([char for char in S if char not in "aeiou"])

# print(result)
