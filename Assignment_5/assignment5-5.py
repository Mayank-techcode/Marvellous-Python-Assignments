def CheckEvenOdd(num):

    if num % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter Number: ")
    value = int(input())

    ret = CheckEvenOdd(value)

    if ret == True:
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()