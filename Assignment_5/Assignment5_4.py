# Accept number from user and print its factorial using for loop

def Factorial(iNo):
    iMul = 1
    for i in range(1, iNo + 1):
        iMul = iMul * i
    return iMul

def main():

    print("Enter a number:")
    iValue = int(input())

    Ret = Factorial(iValue)

    print("Factorial is: ", Ret)

if __name__ == "__main__":
    main()
