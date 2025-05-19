def Largest(no1, no2, no3, no4, no5):

    max = no1

    if no2 > max:
        max = no2
    if no3 > max:
        max = no3
    if no4 > max:
        max = no4
    if no5 > max:
        max = no5

    return max

def main():

    value1 = int(input("Enter 1st number : "))
    value2 = int(input("Enter 2nd number : "))
    value3 = int(input("Enter 3rd number : "))
    value4 = int(input("Enter 4th number : "))
    value5 = int(input("Enter 5th number : "))

    ret = Largest(value1, value2, value3, value4, value5)

    print("Largest Number : ",ret)

if __name__ == "__main__":
    main()