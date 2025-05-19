def CheckPrime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():

    value = int(input("Enter the Number : "))

    ret =  CheckPrime(value)

    if ret == True:
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")

if __name__ == "__main__":
    main()