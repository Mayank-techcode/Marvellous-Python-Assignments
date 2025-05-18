def main():
    num = int(input("Enter a number: "))

    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    main()