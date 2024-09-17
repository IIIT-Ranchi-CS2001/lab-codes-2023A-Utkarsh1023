sentence = input("Enter sentences: ")
sentence = sentence.lower()

words = sentence.split()   # convert string to list

palindrome_count = 0
for word in words:
    is_palindrome = True
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            is_palindrome = False
            break
    if is_palindrome:
        palindrome_count += 1

print("Number of palindrome words:", palindrome_count)
