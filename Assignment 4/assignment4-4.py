from functools import reduce

CheckEven = lambda num : num % 2 == 0
Square = lambda value : value**2
Addition = lambda A, B : A + B

def main():
    print("Enter the number of elements: ")
    size = int(input())

    data = []

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input Data : ", data)

    FData = list(filter(CheckEven, data))
    print("Filter Output : ", FData)

    MData = list(map(Square, FData))
    print("Map Output : ", MData)

    RData = reduce(Addition, MData)
    print("Filter Output : ", RData)


if __name__ == "__main__":
    main()