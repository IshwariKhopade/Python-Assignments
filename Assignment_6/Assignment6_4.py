#Accept 3 numbers from user and print largest using nested if else statements.

def LargestNum(iNo1, iNo2, iNo3):
    if iNo1 >= iNo2:
        if iNo1 >= iNo3:
            print("Largest Number is:", iNo1)
        else:
            print("Largest Number is:", iNo3)
    else:
        if iNo2 >= iNo3:
            print("Largest Number is:", iNo2)
        else:
            print("Largest Number is:", iNo3)

def main():
    print("Enter 1st Number:")
    iValue1 = int(input())

    print("Enter 2nd Number:")
    iValue2 = int(input())

    print("Enter 3rd Number:")
    iValue3 = int(input())

    LargestNum(iValue1, iValue2, iValue3)

if __name__ == "__main__":
    main()