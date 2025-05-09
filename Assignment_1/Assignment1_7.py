# Write a program which contains one function that accepts one number from user and returns true if number is divisible by 5 otherwise return false.

def ChkDivisibility(iNo):
    if(iNo<=0):
        print("Invalid Number, Please Enter a positive number")
    elif(iNo%5 == 0):
        return True
    else:
        return False

def main():

    print("Enter a Number")
    iValue = int(input())

    iAns = ChkDivisibility(iValue)

    print(iAns)

if __name__ == "__main__":
    main()    