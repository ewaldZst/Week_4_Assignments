def IsPalindrome(input):
    reversedInput = ""
    for item in input.lower().strip():
        reversedInput = item + reversedInput

    if input == reversedInput:
        print(f"{input} is a palindrome!")
    else:
        print(f"{input} is NOT a palindrome..")

IsPalindrome("Ball")
IsPalindrome("wow")