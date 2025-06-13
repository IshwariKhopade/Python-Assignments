import ArithmeticModule

def main():
    print("Enter 1st Number")
    fValue1 = float(input())

    print("Enter 2nd Number")
    fValue2 = float(input())

    fARet = ArithmeticModule.Add(fValue1,fValue2)
    print("Addition : " ,fARet)
    fSRet = ArithmeticModule.Sub(fValue1,fValue2)
    print("Subtraction : " ,fSRet)
    fMRet = ArithmeticModule.Mult(fValue1,fValue2)
    print("Multiplication : " ,fMRet)
    fDRet = ArithmeticModule.Div(fValue1,fValue2)
    print("Division : " ,fDRet)

if __name__ == "__main__":
    main()
