def ReversedString(input):
    reversedInput = ""
    for item in input:
        reversedInput = item + reversedInput

    return reversedInput

print(ReversedString("Hi There"))