def check_palindrome(text):
    text = text.lower()
    reversed_text = text[::-1]

    if text == reversed_text:
        return "It is a Palindrome"
    else:
        return "It is not a Palindrome"

word = input("Enter a word: ")
result = check_palindrome(word)
print(result)