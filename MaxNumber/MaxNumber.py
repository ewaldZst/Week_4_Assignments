def MaxNumber(input):
    maxNumber = 0
    for number in input:
        if number > maxNumber:
            maxNumber = number
        else:
            continue
    
    print(maxNumber)

MaxNumber([2, 1, 5, 6, 2, 55, 32, 111, 23])