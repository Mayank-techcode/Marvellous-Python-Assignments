def CheckPrime(num):

    if num < 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True