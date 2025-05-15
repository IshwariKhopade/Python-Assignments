#   Write program which accepts number from user and returns addition of Digits in that Number.

def AddDigit(iNo):

    if iNo == 0:
        print("0")

    iCnt = 0
    imod = 0
    while iNo != 0:
        imod = iNo % 10
        iNo = iNo // 10 
        iCnt = iCnt + imod 
    return iCnt

def main():
    print("Enter a Number:")
    iValue = int(input())

    iRet = AddDigit(iValue)
    print("Addition of Entered Number is:", iRet)

if __name__ == "__main__":
    main()