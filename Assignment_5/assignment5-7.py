def CalculatePerimeter(length, breadth):
    prmtr = 0
    prmtr = 2 * (length + breadth)
    return prmtr

def CalculateArea(length, breadth):
    area = 0
    area = length * breadth
    return area

def main():

    value1 = int(input("Enter Length of Rectangle : "))

    value2 = int(input("Enter Breadth of Rectangle : "))

    ret = CalculateArea(value1, value2)
    print("Area of Rectangle is : ",ret)

    result = CalculatePerimeter(value1, value2)
    print("Perimeter of Rectangle is : ",result)

if __name__ == "__main__":
    main()