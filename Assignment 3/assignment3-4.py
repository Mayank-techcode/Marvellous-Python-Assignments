def Frequency(num, no):
    count = 0

    for i in num:
        if i == no:
            count = count + 1
            
    return count

def main():
    print("Enter number of elements :-")
    size = int(input())

    data = []

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Enter element to search :")
    value = int(input())

    ret = Frequency(data, value)

    print("Frequency of the given number is ",ret)

if __name__ == "__main__":
    main()