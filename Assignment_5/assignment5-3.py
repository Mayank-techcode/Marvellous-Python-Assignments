def CheckEligiblity(value):
    if value >= 18:
        return True
    else:
        return False
    
def main():
    
    num = int(input("Enter Your Age: "))

    ret = CheckEligiblity(num)

    if ret == True:
        print("You are eligible for voting")
    else:
        print("Im sorry please come again when you turn 18")

if __name__ == "__main__":
    main()