def main():
    sum = 0
    for i in range(101):
        if i % 2 == 0:
            sum = sum + i
    
    print("Sum of even numbers: ",sum)

if __name__ == "__main__":
    main()