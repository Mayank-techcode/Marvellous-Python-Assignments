def Factorial(num):

    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def main():

    value = int(input("Enter the number : "))

    ret = Factorial(value)

    print("Factorial of the Number is : ",ret)

if __name__ == "__main__":
    main()