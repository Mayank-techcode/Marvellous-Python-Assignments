def PrimeNo(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True    
    
def main():

    data = []

    size = int(input("Enter the number of elements : "))

    print("Enter the values :-")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    result = list(filter(PrimeNo, data))
    print("Prime Numbers are : ",result)

if __name__ == "__main__":
    main()