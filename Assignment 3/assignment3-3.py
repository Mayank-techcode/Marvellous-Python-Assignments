def Minimum(num):
    min = num[0]
    for i in num:
        if i < min:
            min = i
    return min

def main():
    print("Enter number of elements :-")
    size = int(input())

    data = []

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    ret = Minimum(data)

    print("Minimum number in the list is ",ret)

if __name__ == "__main__":
    main()