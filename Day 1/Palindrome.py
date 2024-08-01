def is_palindrome(s):
    s=s.replace("","").lower()
    return s==s[::-1]
string="A man a plan a canal Panama"
result=is_palindrome(string)
if result:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
