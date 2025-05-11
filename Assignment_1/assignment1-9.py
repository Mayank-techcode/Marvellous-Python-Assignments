def ChkNum(value):
    if value % 2 == 0:
        print(value)

def main():
    count = 0
    num = 1

    while count < 10:
        if num % 2 == 0:
            ChkNum(num)
            count += 1
        num += 1

if __name__ == "__main__":
    main()
