#write a program to check whether the entered number is even or odd.

def ChkEven(iNo):
    if(iNo % 2 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter a Number:")
    iValue = int(input())

    iRet = ChkEven(iValue)

    if(iRet == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()