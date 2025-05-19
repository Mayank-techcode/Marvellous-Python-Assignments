def Largest(no1, no2, no3):
    if no1 > no2:
        if no1 > no3:
            print("Largest Number : ",no1)
        else:
            print("Largest Number : ",no3)
    else:
        if no2 > no3:
            print("Largest number : ",no2)
        else:
            print("Largest Number : ",no3)

def main():
    print("Enter First Number: ")
    value1 = int(input())

    print("Enter Second Number: ")
    value2 = int(input())

    print("Enter Third Number: ")
    value3 = int(input())

    Largest(value1, value2, value3)


if __name__ == "__main__":
    main()