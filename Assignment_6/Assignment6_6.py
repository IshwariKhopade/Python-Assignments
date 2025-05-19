#Accept temperature in celsius and convert it to fahrenheit  F = (C * 9/5) + 32

def CelstoFahren(Cels):
    fahrenheit = ((Cels * (9/5)) +32) 
    return fahrenheit

def main():
    print("Enter Temperature in Celsius:")
    iValue = int(input())

    iRet = CelstoFahren(iValue)

    print("Temperature in Fahrenheit: ", iRet, "f")

if __name__ == "__main__":
    main()