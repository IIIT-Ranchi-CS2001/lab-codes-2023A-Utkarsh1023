num = int(input("Enter any Digits: "))
original_number = num
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print(f"The number is: {original_number}")
print(f"The sum of the digits is: {sum_of_digits}")