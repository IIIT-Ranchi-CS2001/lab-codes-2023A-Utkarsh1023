# Question 3
S3 = input('Enter any String: ')
if(S3 == S3[::-1]):
    print(f"'{S3}' is a Palindrome number.")
else:
    print(f"'{S3}' is not a Palindrome number.")