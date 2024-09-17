import statistics

input_numbers = input("Enter a list of numbers: ")

numbers = [int(num) for num in input_numbers.split()]


print(f"Mean: {statistics.mean(numbers)}")
print(f"Median: {statistics.median(numbers)}")
print(f"Mode: {statistics.mode(numbers)}")
