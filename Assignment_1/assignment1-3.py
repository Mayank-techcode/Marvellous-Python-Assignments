def Addition(no1, no2):
    Ans = 0
    Ans = no1 + no2
    return Ans

def main():
    
    value1 = int(input("Enter First Number: "))
    value2 = int(input("Enter Second Number: "))

    result = Addition(value1, value2)

    print("Addition is : ", result)

if __name__ == "__main__":
    main()