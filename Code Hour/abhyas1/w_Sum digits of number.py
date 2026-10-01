num = input()

sumofn = sum(int(digit) for digit in num)

print(sumofn)   

# or

# Read the integer input from the user
num = int(input())

# Initialize a variable to store the sum of digits
digit_sum = 0

# Loop until the number becomes 0
while num > 0:
    # Get the last digit using the modulo operator (%)
    last_digit = num % 10
    
    # Add the last digit to the total sum
    digit_sum += last_digit
    
    # Remove the last digit from the number using integer division (//)
    num = num // 10

# Print the final sum of the digits
print(digit_sum)
