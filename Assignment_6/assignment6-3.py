def DisplayTable(num):

    for i in range(11):
        ans = num * i
        print(f"{num} * {i} = ",ans)

def main():

    value = int(input("Enter the Number : "))
    
    DisplayTable(value)

if __name__ == "__main__":
    main()