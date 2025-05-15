#   Write program which accepts number from user and returns number of Digits in that Number

def CountDigit(iNo):

    if iNo == 0:
        return 1

    count = 0
    while iNo != 0:
        iNo = iNo // 10 
        count = count + 1
    return count

def main():
    print("Enter a Number:")
    iValue = int(input())

    iRet = CountDigit(iValue)
    print("Digits in Entered Number are:", iRet)

if __name__ == "__main__":
    main()
