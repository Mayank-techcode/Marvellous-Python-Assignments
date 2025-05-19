Even = lambda num : num % 2 == 0

def main():

    data = []

    size = int(input("Enter the number of elements: "))

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    FData = list(filter(Even, data))
    print("Filter Result output : ",FData)

if __name__ == "__main__":
    main()