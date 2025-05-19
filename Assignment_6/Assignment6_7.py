#Accept length and width of rectangle. calculate and display its area and perimeter

def Area(iLen, iWid):
    iArea = iLen * iWid
    return iArea

def Perimeter(iLen, iWid):
    iPeri = 2 * (iLen + iWid)
    return iPeri

def main():
    print("Enter Lenth:")
    iValue1 = int(input())

    print("Enter Width:")
    iValue2 = int(input())

    aRet = Area(iValue1,iValue2)
    pRet = Perimeter(iValue1,iValue2)

    print("Area is: ", aRet)
    print("Perimeter is: ", pRet)

if __name__ == "__main__":
    main()