from Arithmetic import *

def main():
    print("Enter First number: ")
    value1 = int(input())

    print("Enter Second number: ")
    value2 = int(input())

    Ret = Addition(value1, value2)
    print("Results for Addition are: ",Ret)

    Ret = Subtraction(value1, value2)
    print("Results for Subtraction are: ",Ret)
    
    Ret = Multiplication(value1, value2)
    print("Results for Multiplication are: ",Ret)

    Ret = Division(value1, value2)
    print("Results for Division are: ",Ret)

if __name__ == "__main__":
    main()