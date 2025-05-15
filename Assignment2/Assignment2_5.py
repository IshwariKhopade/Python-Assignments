"""
 write program which accepts one number from user and Check given number is prime or not.
 
"""

def ChkPrime(iNo):
    if(iNo<2):
        return False

    for i in range(2,iNo):
        if(iNo % i == 0):
            return False

    return True

def main():
    print("Enter a number:")
    iValue = int(input())

    iRet = ChkPrime(iValue)
    if (iRet == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()