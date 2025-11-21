def CheckIfPrime(number):
    if number <= 1:
        return False
    
    for num in range(2, number):
        if number % num == 0:
            return False
        
    return True


print(CheckIfPrime(3))

print(CheckIfPrime(2))
print(CheckIfPrime(11))
print(CheckIfPrime(15))
print(CheckIfPrime(1))
print(CheckIfPrime(0))


