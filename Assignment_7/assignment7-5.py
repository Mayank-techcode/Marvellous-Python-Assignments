def main():
    text = input("Enter a word or number: ")

    Rtext = text[::-1]

    if text == Rtext:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

if __name__ == "__main__":
    main()