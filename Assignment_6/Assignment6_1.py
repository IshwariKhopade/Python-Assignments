#Write program to accept 2 numbers from user and display their:Sum,Difference,Product,Division

def Sum(iNo1,iNo2):
    return iNo1 + iNo2

def Difference(iNo1,iNo2):
    return iNo1 - iNo2

def Product(iNo1,iNo2):
    return iNo1 * iNo2

def Division(iNo1,iNo2):
    return iNo1 / iNo2

def main():
    print("Enter 1st Number:")
    iValue1 = int(input())

    print("Enter 2nd Number:")
    iValue2 = int(input())

    sRet = Sum(iValue1,iValue2)
    DRet = Difference(iValue1,iValue2)
    pRet = Product(iValue1,iValue2)
    dRet = Division(iValue1,iValue2)

    print("Sum :", sRet)
    print("Difference :", DRet)
    print("Product :", pRet)
    print("Division :", dRet)

if __name__ == "__main__":
    main()