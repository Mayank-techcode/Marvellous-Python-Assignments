def main():
    num = input("Enter a number: ")
    sum = 0

    for digit in num:
        sum = sum + int(digit)

    print("Sum of digits:", sum)

if __name__ == "__main__":
    main()