"""
 write program which accepts one number from user and return it's Factorial.
 
"""

def Fact(iNo):
    iFact = 1
    for i in range (1, iNo+1):
        iFact = iFact * i

    return iFact

def main():
    print("Enter a number:")
    iValue = int(input())

    iRet = Fact(iValue)

    print("Factorial:", iRet)

if __name__ == "__main__":
    main()