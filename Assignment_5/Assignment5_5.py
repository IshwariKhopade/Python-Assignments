# Accept number from user and check whether it is prime or not

def CheckPrime(iNo):

    i = 2
    if(iNo<0):
        iNo = -iNo
    for i in range(2,iNo):
        if((iNo % i) != 0):
            return True
        else:
            return False

def main():

    print("Enter a number:")
    Value = int(input())
    iRet = False

    iRet = CheckPrime(Value)

    if(iRet == True):
        print("It is a prime Number")

    else:
        print("It is not prime Number")


if __name__ == "__main__":
    main()