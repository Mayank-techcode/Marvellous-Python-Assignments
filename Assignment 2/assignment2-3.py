def Factorial(Num):
    fact = 1
    for i in range(1, Num + 1):
        fact = fact * i
    return fact

def main():
    print("Enter the Number : ")
    value = int(input())

    ret = Factorial(value)

    print(f"Factorial is : ",ret)

if __name__ == "__main__":
    main()