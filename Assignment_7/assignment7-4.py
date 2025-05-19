from functools import reduce

Product = lambda A, B : A * B

def main():

    data = []

    size = int(input("Enter the number of elements: "))

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    RData = reduce(Product, data)
    print("Reduce Result output : ",RData)

if __name__ == "__main__":
    main()