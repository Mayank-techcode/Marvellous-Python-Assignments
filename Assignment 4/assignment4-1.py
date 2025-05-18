Power = lambda A : A**2

def main():

    print("Enter the Number: ")
    value = int(input())

    ret = Power(value)

    print("Power of the Number is : ",ret)

if __name__ == "__main__":
    main()