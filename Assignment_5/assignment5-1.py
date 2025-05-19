def Addition(no1, no2):
    ans = no1 + no2
    return ans

def Substraction(no1, no2):
    ans = no1 - no2
    return ans

def Multiplication(no1, no2):
    ans = no1 * no2
    return ans

def Division(no1, no2):
    ans = no1 / no2
    return ans

def main():
    print("Enter First Number: ")
    value1 = int(input())

    print("Enter Second Number: ")
    value2 = int(input())

    ret = Addition(value1, value2)
    print("Addition is : ",ret)

    ret = Substraction(value1, value2)
    print("Addition is : ",ret)

    ret = Multiplication(value1, value2)
    print("Addition is : ",ret)

    ret = Division(value1, value2)
    print("Addition is : ",ret)

if __name__ == "__main__":
    main()