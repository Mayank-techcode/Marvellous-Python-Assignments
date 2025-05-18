def Maximum(num):
    max = 0
    for i in num:
        if i > max:
            max = i
    return max        

def main():

    print("Enter the number of elements : ")
    size = int(input())

    data = []
    
    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)

    ret = Maximum(data)

    print("Maximum number in the list is ",ret)

if __name__ == "__main__":
    main()