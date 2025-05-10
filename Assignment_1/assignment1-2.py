def ChkNum(value):
    if(value % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():

    num = int(input("Enter the Number: "))

    ChkNum(num)

if __name__ == "__main__":
    main()