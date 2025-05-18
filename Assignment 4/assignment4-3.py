from functools import reduce

Range = lambda num : num >= 70 or num == 90
Increase = lambda no : no + 10
Product = lambda A, B : A * B

def main():
    print("Enter the number of elements : ")
    size = int(input())

    data = []

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input data : ",data)

    FData = list(filter(Range, data))
    print("Filter Output : ",FData)

    MData = list(map(Increase, FData))
    print("Filter Output : ",MData)

    RData = reduce(Product, MData)
    print("Filter Output : ",RData)

if __name__ == "__main__":
    main()