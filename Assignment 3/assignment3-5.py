from MarvellousNum import CheckPrime

def ListPrime(value):
    sum = 0

    for i in value:
        if CheckPrime(i) == True:
            sum = sum + i
    return sum

def main():
    print("Enter the number of elements : ")
    size = int(input())

    data = []
    
    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    ret = ListPrime(data)

    print("Addition of all prime numbers is:", ret)

if __name__ == "__main__":
    main()

