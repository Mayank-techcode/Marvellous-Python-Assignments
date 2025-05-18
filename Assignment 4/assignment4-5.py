from functools import reduce

def CheckPrime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def Multiply(no):
    return no * 2

def Maximum(a, b):
    if a > b:
        return a
    else:
        return b        

def main():
    print("Enter the number of elements: ")
    size = int(input())

    data = []

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input Data : ", data)

    FData = list(filter(CheckPrime, data))
    print("Filter Output : ", FData)

    MData = list(map(Multiply, FData))
    print("Map Output : ", MData)

    RData = reduce(Maximum, MData)
    print("Reduce Output : ", RData)


if __name__ == "__main__":
    main()