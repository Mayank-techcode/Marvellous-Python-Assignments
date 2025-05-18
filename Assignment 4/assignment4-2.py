Multiply = lambda A, B : A*B

def main():

    print("Enter First Number: ")
    value1 = int(input())

    print("Enter Second Number: ")
    value2 = int(input())

    ret = Multiply(value1, value2)

    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()