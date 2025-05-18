def Addition(num):
    sum = 0
    for i in num:
        sum = sum + int(i)
    return sum

def main():

    print("Number of elements in the list: ")
    size = int(input())

    data = []
    
    print("Enter the values :- ")
    for i in range(size):
        no = int(input())
        data.append(no)

    ret = Addition(data)

    print("Sum of all values in list : ",ret)

if __name__ == "__main__":
    main()