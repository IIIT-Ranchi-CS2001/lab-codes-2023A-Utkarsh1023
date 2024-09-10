string = input("Enter a string: ")
character = input("Enter the character to count: ")

count = 0

for char in string:
    if char == character:
        count += 1

print(f"The character '{character}' occurs {count} times in the string '{string}'.")