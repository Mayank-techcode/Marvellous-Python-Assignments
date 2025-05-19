Square = lambda num : num**2
Cube = lambda num : num**3

def main():

    value = int(input("Enter the Number: "))

    print(f"Square of {value} is : ",Square(value))

    print(f"Cube of {value} is : ",Cube(value))

if __name__ == "__main__":
    main()