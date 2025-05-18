def CheckPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def main():
    print("Enter the Number: ")
    value = int(input())

    ret = CheckPrime(value)

    if ret:
        print("It is a Prime Number")
    else:
        print("Not a Prime Number")

if __name__ == "__main__":
    main()
