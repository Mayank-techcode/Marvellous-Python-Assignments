def ConvertFahrenheit(cel):
    fah =  (cel * 9/5) + 32
    return fah

def main():

    print("Enter Temperature in Celsius :-")
    value = int(input())

    ret = ConvertFahrenheit(value)

    print("Temperature in Fahrenheit : ",ret,"°F")

if __name__ == "__main__":
    main()