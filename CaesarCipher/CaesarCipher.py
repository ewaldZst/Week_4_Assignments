def Cipher(input, shift):
    output = ""
    for char in input:
    
        if char.isalpha():
            if char.isupper():
                beginning = ord("A")
            else:
                beginning = ord("a")
        
            offset = (ord(char) - beginning + shift) % 26
            output += chr(beginning + offset)
        else:
            output += char


    return output

print(Cipher("Hi, there!", 1))