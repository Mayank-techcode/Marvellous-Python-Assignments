def ChkNum(value):
    if(value == 0):
        print("Zero")
    elif(value < 0):
        print("Negative number")
    else:
        print("Positive number")

def main():

    num = int(input("Enter the Number: "))

    ChkNum(num)

if __name__ == "__main__":
    main()