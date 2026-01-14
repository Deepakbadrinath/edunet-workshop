def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
max_digit_number = int('9' * 10) 
max_sum = sum_of_digits(max_digit_number)

print("10-digit number with the highest sum of digits:", max_digit_number)
print("Highest sum of digits:", max_sum)