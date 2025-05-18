def SumFactors(Num):
    sum = 0
    for i in range(1, Num):
        if Num % i == 0:
            sum = sum + i
    return sum

def main():
    print("Enter the Number: ")
    value = int(input())

    ret = SumFactors(value)

    print("Addition of Factors are : ", ret)

if __name__ == "__main__":
    main()