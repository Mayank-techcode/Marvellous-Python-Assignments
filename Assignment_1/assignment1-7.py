def ChkNum(value):
    if(value % 5 == 0):
        print("True")
    else:
        print("False")

def main():

    num = int(input("Enter the Number: "))

    ChkNum(num)

if __name__ == "__main__":
    main()