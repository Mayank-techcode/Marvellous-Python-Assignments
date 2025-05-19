def CheckVowel(value):
    if value.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def main():
    char = input("Enter the character: ")
    
    ret = CheckVowel(char)

    if ret == True:
        print(char+ " is a vowel")
    else:
        print(char+ " is a consonent")

if __name__ == "__main__":
    main()
