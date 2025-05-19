Double = lambda num : num * 2

def main():

    data = []

    size = int(input("Enter the number of elements: "))

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    MData = list(map(Double, data))
    print("Map Result output : ",MData)

if __name__ == "__main__":
    main()