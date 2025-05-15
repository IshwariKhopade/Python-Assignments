"""
 write program which accepts one number from user and return Addition of it's Factors.
 
"""

def Factors(iNo):
    iSum = 0
    for i in range (1,iNo):
        if(iNo % i == 0):
            iSum = iSum + i  

    return iSum

def main():
    print("Enter a number:")
    iValue = int(input())

    iRet = Factors(iValue)

    print("Addition of Factors is:", iRet)

if __name__ == "__main__":
    main()